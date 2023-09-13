from gensim.models import Word2Vec
from nltk import wordpunct_tokenize, sent_tokenize
from resources import contractions
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from sklearn.decomposition import PCA
from random import shuffle
from datetime import datetime
import numpy as np
import re

       # START
        
        # org this
        self.btn_add_input.clicked.connect(self.handle_manual_input)
        self.btn_search_list.clicked.connect(self.search_list)
        self.lst_vocab.itemSelectionChanged.connect(self.selection_change)
        self.btn_create_ext_sim_plot.clicked.connect(self.show_sim_plot_external)
        self.btn_create_ext_ran_plot.clicked.connect(self.show_ran_plot_external)
        self.btn_refresh_ran_plot.clicked.connect(self.show_ran_plot)
        self.cmb_num_sim_plot.currentIndexChanged.connect(self.show_sim_plot)
        self.cmb_num_ran_plot.currentIndexChanged.connect(self.show_ran_plot)
        self.tab_bottom_left.currentChanged.connect(self.tabs_bottom_left_changed)
        self.btn_upload_file.clicked.connect(self.handle_upload_file)
        self.btn_math_equal.clicked.connect(self.do_the_math)
        self.btn_clear_input.clicked.connect(self.debug)
        self.btn_load_snapshots.clicked.connect(self.first_snapshot)
        self.btn_next_snap.clicked.connect(self.next_snapshot)
        self.btn_prev_snap.clicked.connect(self.prev_snapshot)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_sort.clicked.connect(self.sort_vocab_list)

        self.voc = []
        self.model = 0

        self.chunk_count = 5
        self.model_snapshots = []

        self.snap_pos = 0

        # see sort_vocab_list()
        self.list_sort = 0

        self.tbl_similar.setColumnCount(2)
        self.cmb_chunk_count.setCurrentIndex(2)

    def sort_vocab_list(self):
        
        self.lst_vocab.clear()
        
        # toggle 0 -> 1, 1 -> 2, 2 -> 0
        self.list_sort = (self.list_sort + 1) % 3
        
        # default
        if self.list_sort == 0:
            self.lst_vocab.addItems(list(self.model.wv.vocab.keys()))
        
        # A -> Z
        elif self.list_sort == 1:
            self.lst_vocab.addItems(sorted(list(self.model.wv.vocab.keys())))
        
        # Z -> A
        else:
            self.lst_vocab.addItems(sorted(list(self.model.wv.vocab.keys()), reverse=True)) 

    def reset(self):

        if self.hrz_similarity_plot.count() > 0:
            self.hrz_similarity_plot.removeWidget(self.sim_plot)

        if self.hrz_random_plot.count() > 0:
            self.hrz_random_plot.removeWidget(self.ran_plot)

        if self.hrz_snap_plots.count() > 0:
            self.hrz_snap_plots.removeWidget(self.snap_plot)
        
        fig = Figure()

        self.sim_plot, self.ran_plot, self.snap_plot = FigureCanvas(fig), FigureCanvas(fig), FigureCanvas(fig)
        
        self.hrz_similarity_plot.addWidget(self.sim_plot)
        self.hrz_random_plot.addWidget(self.ran_plot)
        self.hrz_snap_plots.addWidget(self.snap_plot)
        self.sim_plot.draw()
        self.ran_plot.draw()
        self.snap_plot.draw()

        self.voc = []
        self.model = 0
        self.model_snapshots = []
        self.snap_pos = 0
        self.lbl_selected_word.setText('Selected word: NONE')
        self.lbl_vocab_size.setText('Vocab size: 0')
        self.lst_vocab.clear()
        self.label.setText('')
        self.cmb_word_one.clear()
        self.cmb_word_two.clear()
        self.lbl_snapshot.setText('')
        self.lbl_add_word_one.setText('')
        self.lbl_add_word_two.setText('')
        self.lbl_add_result.setText('')
        self.lbl_sub_word_one.setText('')
        self.lbl_sub_word_two.setText('')
        self.lbl_sub_result.setText('')

        self.write_to_log('--RESET--')

        self.tabs_other_options.setCurrentIndex(0)

    def get_time(self):
        # to be used with write_to_log()

        return datetime.now().strftime('%H:%M:%S')
    
    def write_to_log(self, msg):
        # write info, errors, etc. to the screen

        self.lst_log.addItem(f'[{self.get_time()}] {msg}')
        self.lst_log.scrollToBottom()

    def load_snapshot(self, change):

        try:
            if self.hrz_snap_plots.count() > 0:
                self.hrz_snap_plots.removeWidget(self.snap_plot)

            n_words = 10
            target = self.lst_vocab.selectedItems()[0].text()

            all_plot_data = []

            self.snap_pos += change
            self.snap_pos %= len(self.model_snapshots)
            mdl = self.model_snapshots[self.snap_pos]
            
            similar_words = [pair[0] for pair in mdl.wv.similar_by_word(target, topn=n_words)]
            plot_data = [(target, mdl.wv.get_vector(target))]
            plot_data.extend( [(w, mdl.wv.get_vector(w)) for w in similar_words] )
            plot_data = np.array(plot_data)
            labels = plot_data[:,0]
            feats_pca = PCA(n_components=2).fit_transform(list(plot_data[:,1]))

            fig = Figure()
            ax = fig.add_subplot(111)

            for i in range(len(feats_pca)):
                ax.plot(feats_pca[:,0][i], feats_pca[:,1][i], 'wh')
                    
                if labels[i] == target:
                    ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i], color='red')
                else:
                    ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i])
                
                ax.axis('off')

            self.snap_plot = FigureCanvas(fig)
            self.hrz_snap_plots.addWidget(self.snap_plot)
            self.snap_plot.draw()

            self.lbl_snapshot.setText(f'Snapshot {self.snap_pos+1}/{len(self.model_snapshots)}')

        except KeyError:
            self.write_to_log(f'skipping snap #{self.snap_pos+1}, "{target}" not in model')
            
            if change < 0:
                self.prev_snapshot()
            else:
                self.next_snapshot()
            

        except IndexError:
            self.write_to_log('select a word to view snapshots')

        except Exception as e:
            print(e)

    def first_snapshot(self):
        self.snap_pos = 0
        self.load_snapshot(0)

    def next_snapshot(self):
        self.load_snapshot(1)

    def prev_snapshot(self):
        self.load_snapshot(-1)

    def do_the_math(self):
        
        try:
            inputs = (self.cmb_word_one.currentText(), self.cmb_word_two.currentText())

            res_add = self.model.wv.get_vector(inputs[0]) + \
                      self.model.wv.get_vector(inputs[1])

            res_sub = self.model.wv.get_vector(inputs[0]) - \
                      self.model.wv.get_vector(inputs[1])
            
            res_add = self.model.wv.similar_by_vector(res_add)
            res_sub = self.model.wv.similar_by_vector(res_sub)

            res_add = [word for (word,_) in res_add if word not in inputs][0]
            res_sub = [word for (word,_) in res_sub if word not in inputs][0]

            self.lbl_add_word_one.setText(inputs[0])
            self.lbl_sub_word_one.setText(inputs[0])
            self.lbl_add_word_two.setText(inputs[1])
            self.lbl_sub_word_two.setText(inputs[1])
            self.lbl_add_result.setText(res_add)
            self.lbl_sub_result.setText(res_sub)

        except Exception as e:
            print(e)

    def handle_upload_file(self):
        try:
            file_path = QtWidgets.QFileDialog.getOpenFileName()[0]
            
            file_text = open(file_path, 'r', encoding='utf8').read()

            file_text = re.sub(r'\n', ' ', file_text)
            file_text = re.sub(r'\s+', ' ', file_text)

            sentences = [i for x in [x.split('\n') for x in sent_tokenize(file_text)] for i in x]
            sentences = [[x for x in wordpunct_tokenize(' '.join([(contractions[s.lower()] if s.lower() in contractions else s.lower()) for s in sent.split()])) if str.isalnum(x)] for sent in sentences]

            self.add_to_vocab(sentences)
        
        except:
            self.write_to_log('error selecting file')

    def handle_manual_input(self):
        if len(self.txt_input.toPlainText()) > 0:
            sentences = [i for x in [x.split('\n') for x in sent_tokenize(self.txt_input.toPlainText())] for i in x]
            sentences = [[x for x in wordpunct_tokenize(' '.join([(contractions[s.lower()] if s.lower() in contractions else s.lower()) for s in sent.split()])) if str.isalnum(x)] for sent in sentences]

            self.add_to_vocab(sentences)

    def show_sim_plot_external(self):
        self.show_sim_plot(embedded=False)
    
    def show_ran_plot_external(self):
        self.show_ran_plot(embedded=False)

    def debug(self):
        self.statusbar.showMessage("DEBUG!")

    def tabs_bottom_left_changed(self):
        if self.tab_bottom_left.currentIndex() == 0:
            self.show_sim_plot()
        elif self.tab_bottom_left.currentIndex() == 1:
            self.show_ran_plot()
        
    def add_to_vocab(self, sentences):

        self.write_to_log('adding vocab to model')

        self.chunk_count = int(self.cmb_chunk_count.currentText())

        if len(sentences) < self.chunk_count:
            self.voc.extend(sentences)
            self.model = Word2Vec(self.voc, min_count=1)
            self.model_snapshots.append(self.model)

            self.write_to_log('model created, (1 snapshot)')
        
        else:
            min_chunk = len(sentences) // self.chunk_count
            extra = (len(sentences) % self.chunk_count)

            chunks = []

            for i in range(self.chunk_count):
                if len(chunks) == 0:
                    chunks.append( sentences[:min_chunk] )
                else:
                    if extra > 0:
                        chunks.append( sentences[:len(chunks[-1])+min_chunk+1] )
                        extra -= 1
                    else:
                        chunks.append( sentences[:len(chunks[-1])+min_chunk] )

            for chunk in chunks:
                self.voc.extend(chunk)
                self.model = Word2Vec(self.voc, min_count=1)
                self.model_snapshots.append(self.model)

            self.write_to_log(f'model created, ({self.chunk_count} snapshots)')

        self.txt_input.clear()
        self.lst_vocab.clear()

        self.lst_vocab.addItems(list(self.model.wv.vocab.keys()))
        self.lbl_vocab_size.setText(f'Vocab size: {len(list(self.model.wv.vocab.keys()))}')

        # work this out, only update things when needed
        self.update()

    def search_list(self):
        self.lst_vocab.clear()
        self.lst_vocab.addItems([w for w in list(self.model.wv.vocab.keys()) if re.search(self.txt_search.text(), w, re.IGNORECASE)])

    def selection_change(self):
        try:
            word = self.lst_vocab.selectedItems()[0].text()
            self.update()
        except:
            word = "NONE"
        
        self.lbl_selected_word.setText(f"Selected word: {word}")
        self.tabs_bottom_left_changed()
        self.show_details()
        self.build_similar_table()
            
    def update(self):
        self.cmb_word_one.clear()
        self.cmb_word_two.clear()
        self.cmb_word_one.addItems(sorted(list(self.model.wv.vocab.keys())))
        self.cmb_word_two.addItems(sorted(list(self.model.wv.vocab.keys())))    

    def show_details(self):
        try:
            out = self.lst_vocab.selectedItems()[0].text()
            out += '\n\n' + str(self.model.wv.get_vector(out))
            self.label.setText(out)
        except:
            pass

    def show_sim_plot(self, n_words=10, embedded=True): 
        try:
            if self.hrz_similarity_plot.count() > 0:
                self.hrz_similarity_plot.removeWidget(self.sim_plot)
        
            n_words = int(self.cmb_num_sim_plot.currentText())

            target = self.lst_vocab.selectedItems()[0].text()
            similar_words = [pair[0] for pair in self.model.wv.similar_by_word(target, topn=n_words)]

            plot_data = [(target, self.model.wv.get_vector(target))]
            plot_data.extend( [(w, self.model.wv.get_vector(w)) for w in similar_words] )

            plot_data = np.array(plot_data)

            labels = plot_data[:,0]
            feats = plot_data[:,1]

            feats_pca = PCA(n_components=2).fit_transform(list(feats))
            
            if embedded:
                fig = Figure()
                ax = fig.add_subplot(111)

                for i in range(len(feats_pca)):
                    ax.plot(feats_pca[:,0][i], feats_pca[:,1][i], 'wh')
                    
                    if labels[i] == target:
                        ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i], color='red')
                    else:
                        ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i])
                
                ax.axis('off')

                self.sim_plot = FigureCanvas(fig)
                self.hrz_similarity_plot.addWidget(self.sim_plot)
                self.sim_plot.draw()
            
            else:
                ax = plt.subplot(1,1,1)

                for i in range(len(feats_pca)):
                    ax.plot(feats_pca[:,0][i], feats_pca[:,1][i], 'wh')
                    
                    if labels[i] == target:
                        ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i], color='red')
                    else:
                        ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i])

                plt.show()

        except Exception as e:
            print(e)

    def show_ran_plot(self, n_words=10, embedded=True):
        try:
            if self.hrz_random_plot.count() > 0:
                self.hrz_random_plot.removeWidget(self.ran_plot)

            n_words = int(self.cmb_num_ran_plot.currentText())

            words = list(self.model.wv.vocab.keys())

            shuffle(words)

            words = words[:n_words]

            plot_data = np.array( [(w, self.model.wv.get_vector(w)) for w in words] )

            labels = plot_data[:,0]
            feats = plot_data[:,1]

            feats_pca = PCA(n_components=2).fit_transform(list(feats))

            if embedded:
                fig = Figure()
                ax = fig.add_subplot(111)

                for i in range(len(feats_pca)):
                    ax.plot(feats_pca[:,0][i], feats_pca[:,1][i], 'wh')
                    
                    ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i])
                
                ax.axis('off')

                self.ran_plot = FigureCanvas(fig)
                self.hrz_random_plot.addWidget(self.ran_plot)
                self.ran_plot.draw()
            
            else:
                ax = plt.subplot(1,1,1)

                for i in range(len(feats_pca)):
                    ax.plot(feats_pca[:,0][i], feats_pca[:,1][i], 'wh')
                    
                    ax.text(feats_pca[:,0][i], feats_pca[:,1][i], labels[i])

                plt.show()

        except Exception as e:
            print(e)

    def build_similar_table(self):
        try:
            sim = self.model.wv.most_similar(self.lst_vocab.selectedItems()[0].text(), topn=7)
            self.tbl_similar.setRowCount(len(sim))
            for i,pair in enumerate(sim):
                self.tbl_similar.setItem(i,0,QtWidgets.QTableWidgetItem(pair[0]))
                self.tbl_similar.setItem(i,1,QtWidgets.QTableWidgetItem(str(pair[1])))
        except:
            pass