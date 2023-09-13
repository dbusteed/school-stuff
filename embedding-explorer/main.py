# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gensim.models import Word2Vec
from nltk import wordpunct_tokenize, sent_tokenize
from resources.resources import contractions
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

class Ui_win_main(object):
    def setupUi(self, win_main):
        win_main.setObjectName("win_main")
        win_main.resize(1100, 800)
        win_main.setMaximumSize(QtCore.QSize(1100, 800))
        self.wgt_main = QtWidgets.QWidget(win_main)
        self.wgt_main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt_main.sizePolicy().hasHeightForWidth())
        self.wgt_main.setSizePolicy(sizePolicy)
        self.wgt_main.setMinimumSize(QtCore.QSize(0, 0))
        self.wgt_main.setMaximumSize(QtCore.QSize(1100, 800))
        self.wgt_main.setObjectName("wgt_main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.wgt_main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1101, 771))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hrz_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hrz_main.setContentsMargins(5, 3, 5, 3)
        self.hrz_main.setObjectName("hrz_main")
        self.vrt_left = QtWidgets.QVBoxLayout()
        self.vrt_left.setObjectName("vrt_left")
        self.hrz_top_left = QtWidgets.QHBoxLayout()
        self.hrz_top_left.setObjectName("hrz_top_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txt_search = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_search.setObjectName("txt_search")
        self.horizontalLayout_3.addWidget(self.txt_search)
        self.btn_search_list = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search_list.sizePolicy().hasHeightForWidth())
        self.btn_search_list.setSizePolicy(sizePolicy)
        self.btn_search_list.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_search_list.setObjectName("btn_search_list")
        self.horizontalLayout_3.addWidget(self.btn_search_list)
        self.btn_sort = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sort.sizePolicy().hasHeightForWidth())
        self.btn_sort.setSizePolicy(sizePolicy)
        self.btn_sort.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_sort.setObjectName("btn_sort")
        self.horizontalLayout_3.addWidget(self.btn_sort)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lst_vocab = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lst_vocab.setObjectName("lst_vocab")
        self.verticalLayout_2.addWidget(self.lst_vocab)
        self.hrz_top_left.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_selected_word = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_selected_word.setFont(font)
        self.lbl_selected_word.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_selected_word.setObjectName("lbl_selected_word")
        self.horizontalLayout_2.addWidget(self.lbl_selected_word)
        self.lbl_vocab_size = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_vocab_size.setFont(font)
        self.lbl_vocab_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_vocab_size.setObjectName("lbl_vocab_size")
        self.horizontalLayout_2.addWidget(self.lbl_vocab_size)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabs_deets = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabs_deets.setObjectName("tabs_deets")
        self.tab_embed = QtWidgets.QWidget()
        self.tab_embed.setObjectName("tab_embed")
        self.lbl_word = QtWidgets.QLabel(self.tab_embed)
        self.lbl_word.setGeometry(QtCore.QRect(20, 10, 451, 31))
        self.lbl_word.setText("")
        self.lbl_word.setObjectName("lbl_word")
        self.txt_embedding = QtWidgets.QTextBrowser(self.tab_embed)
        self.txt_embedding.setGeometry(QtCore.QRect(15, 51, 461, 241))
        self.txt_embedding.setObjectName("txt_embedding")
        self.tabs_deets.addTab(self.tab_embed, "")
        self.tab_similar = QtWidgets.QWidget()
        self.tab_similar.setObjectName("tab_similar")
        self.tbl_similar = QtWidgets.QTableWidget(self.tab_similar)
        self.tbl_similar.setGeometry(QtCore.QRect(0, 0, 491, 311))
        self.tbl_similar.setObjectName("tbl_similar")
        self.tbl_similar.setColumnCount(0)
        self.tbl_similar.setRowCount(0)
        self.tbl_similar.horizontalHeader().setStretchLastSection(True)
        self.tabs_deets.addTab(self.tab_similar, "")
        self.verticalLayout_3.addWidget(self.tabs_deets)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 12)
        self.hrz_top_left.addLayout(self.verticalLayout_3)
        self.hrz_top_left.setStretch(0, 1)
        self.hrz_top_left.setStretch(1, 2)
        self.vrt_left.addLayout(self.hrz_top_left)
        self.tab_bottom_left = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tab_bottom_left.setEnabled(True)
        self.tab_bottom_left.setTabsClosable(False)
        self.tab_bottom_left.setObjectName("tab_bottom_left")
        self.tab_chart_one = QtWidgets.QWidget()
        self.tab_chart_one.setObjectName("tab_chart_one")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_chart_one)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 10, 471, 321))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hrz_similarity_plot = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hrz_similarity_plot.setContentsMargins(0, 0, 0, 0)
        self.hrz_similarity_plot.setObjectName("hrz_similarity_plot")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_chart_one)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(529, 90, 171, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cmb_num_sim_plot = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.cmb_num_sim_plot.setObjectName("cmb_num_sim_plot")
        self.cmb_num_sim_plot.addItem("")
        self.cmb_num_sim_plot.addItem("")
        self.cmb_num_sim_plot.addItem("")
        self.cmb_num_sim_plot.addItem("")
        self.horizontalLayout.addWidget(self.cmb_num_sim_plot)
        self.btn_create_ext_sim_plot = QtWidgets.QPushButton(self.tab_chart_one)
        self.btn_create_ext_sim_plot.setGeometry(QtCore.QRect(550, 180, 131, 28))
        self.btn_create_ext_sim_plot.setObjectName("btn_create_ext_sim_plot")
        self.line_7 = QtWidgets.QFrame(self.tab_chart_one)
        self.line_7.setGeometry(QtCore.QRect(490, 10, 20, 321))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.tab_bottom_left.addTab(self.tab_chart_one, "")
        self.tab_chart_two = QtWidgets.QWidget()
        self.tab_chart_two.setObjectName("tab_chart_two")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_chart_two)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 471, 321))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.hrz_random_plot = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.hrz_random_plot.setContentsMargins(0, 0, 0, 0)
        self.hrz_random_plot.setObjectName("hrz_random_plot")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_chart_two)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(530, 90, 171, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cmb_num_ran_plot = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.cmb_num_ran_plot.setObjectName("cmb_num_ran_plot")
        self.cmb_num_ran_plot.addItem("")
        self.cmb_num_ran_plot.addItem("")
        self.cmb_num_ran_plot.addItem("")
        self.cmb_num_ran_plot.addItem("")
        self.horizontalLayout_4.addWidget(self.cmb_num_ran_plot)
        self.btn_create_ext_ran_plot = QtWidgets.QPushButton(self.tab_chart_two)
        self.btn_create_ext_ran_plot.setGeometry(QtCore.QRect(550, 180, 131, 28))
        self.btn_create_ext_ran_plot.setObjectName("btn_create_ext_ran_plot")
        self.btn_refresh_ran_plot = QtWidgets.QPushButton(self.tab_chart_two)
        self.btn_refresh_ran_plot.setGeometry(QtCore.QRect(550, 220, 131, 28))
        self.btn_refresh_ran_plot.setObjectName("btn_refresh_ran_plot")
        self.line_6 = QtWidgets.QFrame(self.tab_chart_two)
        self.line_6.setGeometry(QtCore.QRect(490, 10, 20, 321))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.tab_bottom_left.addTab(self.tab_chart_two, "")
        self.tab_snapshots = QtWidgets.QWidget()
        self.tab_snapshots.setEnabled(True)
        self.tab_snapshots.setObjectName("tab_snapshots")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_snapshots)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(9, 9, 471, 321))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.hrz_snap_plots = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.hrz_snap_plots.setContentsMargins(0, 0, 0, 0)
        self.hrz_snap_plots.setObjectName("hrz_snap_plots")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_snapshots)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 70, 197, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_snapshot = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_snapshot.setFont(font)
        self.lbl_snapshot.setText("")
        self.lbl_snapshot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_snapshot.setObjectName("lbl_snapshot")
        self.verticalLayout.addWidget(self.lbl_snapshot)
        self.btn_load_snapshots = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_load_snapshots.setEnabled(True)
        self.btn_load_snapshots.setCheckable(False)
        self.btn_load_snapshots.setObjectName("btn_load_snapshots")
        self.verticalLayout.addWidget(self.btn_load_snapshots)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_prev_snap = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_prev_snap.setObjectName("btn_prev_snap")
        self.horizontalLayout_8.addWidget(self.btn_prev_snap)
        self.btn_next_snap = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_next_snap.setObjectName("btn_next_snap")
        self.horizontalLayout_8.addWidget(self.btn_next_snap)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line_5 = QtWidgets.QFrame(self.tab_snapshots)
        self.line_5.setGeometry(QtCore.QRect(490, 10, 20, 321))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.tab_bottom_left.addTab(self.tab_snapshots, "")
        self.tab_math = QtWidgets.QWidget()
        self.tab_math.setObjectName("tab_math")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_math)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 731, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cmb_word_one = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmb_word_one.setObjectName("cmb_word_one")
        self.horizontalLayout_5.addWidget(self.cmb_word_one)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.cmb_word_two = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmb_word_two.setObjectName("cmb_word_two")
        self.horizontalLayout_5.addWidget(self.cmb_word_two)
        self.btn_math_equal = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_math_equal.setObjectName("btn_math_equal")
        self.horizontalLayout_5.addWidget(self.btn_math_equal)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 3)
        self.horizontalLayout_5.setStretch(4, 3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_add_word_one = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_add_word_one.setText("")
        self.lbl_add_word_one.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add_word_one.setObjectName("lbl_add_word_one")
        self.horizontalLayout_7.addWidget(self.lbl_add_word_one)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lbl_add_word_two = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_add_word_two.setText("")
        self.lbl_add_word_two.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add_word_two.setObjectName("lbl_add_word_two")
        self.horizontalLayout_7.addWidget(self.lbl_add_word_two)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lbl_add_result = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_add_result.setText("")
        self.lbl_add_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add_result.setObjectName("lbl_add_result")
        self.horizontalLayout_7.addWidget(self.lbl_add_result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_sub_word_one = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_sub_word_one.setText("")
        self.lbl_sub_word_one.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub_word_one.setObjectName("lbl_sub_word_one")
        self.horizontalLayout_6.addWidget(self.lbl_sub_word_one)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.lbl_sub_word_two = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_sub_word_two.setText("")
        self.lbl_sub_word_two.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub_word_two.setObjectName("lbl_sub_word_two")
        self.horizontalLayout_6.addWidget(self.lbl_sub_word_two)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lbl_sub_result = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_sub_result.setText("")
        self.lbl_sub_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub_result.setObjectName("lbl_sub_result")
        self.horizontalLayout_6.addWidget(self.lbl_sub_result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(2, 4)
        self.verticalLayout_4.setStretch(4, 4)
        self.tab_bottom_left.addTab(self.tab_math, "")
        self.vrt_left.addWidget(self.tab_bottom_left)
        self.vrt_left.setStretch(0, 2)
        self.vrt_left.setStretch(1, 2)
        self.hrz_main.addLayout(self.vrt_left)
        self.vrt_right = QtWidgets.QVBoxLayout()
        self.vrt_right.setContentsMargins(-1, -1, -1, 0)
        self.vrt_right.setObjectName("vrt_right")
        self.vrt_inputs = QtWidgets.QVBoxLayout()
        self.vrt_inputs.setContentsMargins(-1, -1, -1, 0)
        self.vrt_inputs.setObjectName("vrt_inputs")
        self.vrt_manual_input = QtWidgets.QVBoxLayout()
        self.vrt_manual_input.setContentsMargins(9, 5, 9, -1)
        self.vrt_manual_input.setObjectName("vrt_manual_input")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.vrt_manual_input.addWidget(self.label_7)
        self.txt_input = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_input.setFont(font)
        self.txt_input.setObjectName("txt_input")
        self.vrt_manual_input.addWidget(self.txt_input)
        self.hrz_manual_input_btns = QtWidgets.QHBoxLayout()
        self.hrz_manual_input_btns.setContentsMargins(15, -1, 15, -1)
        self.hrz_manual_input_btns.setObjectName("hrz_manual_input_btns")
        self.btn_add_input = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_add_input.setObjectName("btn_add_input")
        self.hrz_manual_input_btns.addWidget(self.btn_add_input)
        self.btn_clear_input = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_clear_input.setObjectName("btn_clear_input")
        self.hrz_manual_input_btns.addWidget(self.btn_clear_input)
        self.hrz_manual_input_btns.setStretch(0, 2)
        self.hrz_manual_input_btns.setStretch(1, 1)
        self.vrt_manual_input.addLayout(self.hrz_manual_input_btns)
        self.vrt_inputs.addLayout(self.vrt_manual_input)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.hrz_upload_input = QtWidgets.QHBoxLayout()
        self.hrz_upload_input.setContentsMargins(5, -1, 5, -1)
        self.hrz_upload_input.setSpacing(20)
        self.hrz_upload_input.setObjectName("hrz_upload_input")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.hrz_upload_input.addWidget(self.label_4)
        self.btn_upload_file = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_upload_file.setObjectName("btn_upload_file")
        self.hrz_upload_input.addWidget(self.btn_upload_file)
        self.hrz_upload_input.setStretch(0, 1)
        self.hrz_upload_input.setStretch(1, 6)
        self.verticalLayout_5.addLayout(self.hrz_upload_input)
        self.vrt_inputs.addLayout(self.verticalLayout_5)
        self.vrt_right.addLayout(self.vrt_inputs)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.vrt_right.addWidget(self.line_2)
        self.tabs_other_options = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabs_other_options.setObjectName("tabs_other_options")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lst_log = QtWidgets.QListWidget(self.tab)
        self.lst_log.setGeometry(QtCore.QRect(10, 11, 300, 201))
        self.lst_log.setObjectName("lst_log")
        self.tabs_other_options.addTab(self.tab, "")
        self.tab_options = QtWidgets.QWidget()
        self.tab_options.setObjectName("tab_options")
        self.groupBox = QtWidgets.QGroupBox(self.tab_options)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 151, 131))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 131, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.chk_create_snaps = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.chk_create_snaps.setChecked(True)
        self.chk_create_snaps.setObjectName("chk_create_snaps")
        self.verticalLayout_6.addWidget(self.chk_create_snaps)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.cmb_chunk_count = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.cmb_chunk_count.setObjectName("cmb_chunk_count")
        self.cmb_chunk_count.addItem("")
        self.cmb_chunk_count.addItem("")
        self.cmb_chunk_count.addItem("")
        self.cmb_chunk_count.addItem("")
        self.cmb_chunk_count.addItem("")
        self.horizontalLayout_9.addWidget(self.cmb_chunk_count)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_options)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 151, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_reset = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_reset.setGeometry(QtCore.QRect(20, 20, 121, 28))
        self.btn_reset.setObjectName("btn_reset")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_options)
        self.groupBox_3.setGeometry(QtCore.QRect(169, 9, 141, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 101, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_save_model = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_save_model.setObjectName("btn_save_model")
        self.verticalLayout_7.addWidget(self.btn_save_model)
        self.btn_load_model = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_load_model.setObjectName("btn_load_model")
        self.verticalLayout_7.addWidget(self.btn_load_model)
        self.tabs_other_options.addTab(self.tab_options, "")
        self.vrt_right.addWidget(self.tabs_other_options)
        self.vrt_right.setStretch(0, 2)
        self.vrt_right.setStretch(1, 1)
        self.vrt_right.setStretch(2, 1)
        self.hrz_main.addLayout(self.vrt_right)
        self.hrz_main.setStretch(0, 7)
        self.hrz_main.setStretch(1, 3)
        win_main.setCentralWidget(self.wgt_main)
        self.statusbar = QtWidgets.QStatusBar(win_main)
        self.statusbar.setObjectName("statusbar")
        win_main.setStatusBar(self.statusbar)

        self.retranslateUi(win_main)
        self.tabs_deets.setCurrentIndex(0)
        self.tab_bottom_left.setCurrentIndex(0)
        self.cmb_num_sim_plot.setCurrentIndex(1)
        self.cmb_num_ran_plot.setCurrentIndex(1)
        self.tabs_other_options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(win_main)

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
        self.btn_clear_input.clicked.connect(self.clear_input)
        self.btn_load_snapshots.clicked.connect(self.first_snapshot)
        self.btn_next_snap.clicked.connect(self.next_snapshot)
        self.btn_prev_snap.clicked.connect(self.prev_snapshot)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_sort.clicked.connect(self.sort_vocab_list)
        self.btn_save_model.clicked.connect(self.save_model)
        self.btn_load_model.clicked.connect(self.load_model)

        self.voc = []
        self.model = 0

        self.chunk_count = 5
        self.model_snapshots = []

        self.snap_pos = 0

        # see sort_vocab_list()
        self.list_sort = 0

        self.tbl_similar.setColumnCount(2)
        self.cmb_chunk_count.setCurrentIndex(2)

    def save_model(self):
        try:
            file_path = QtWidgets.QFileDialog.getSaveFileName(caption='Save Embedding Model',
                directory="models/",
                filter="Models (*.model)",
                initialFilter="Models (*.model)")[0]

            self.model.save(file_path)
            self.write_to_log(f'model saved to {file_path}')
        
        except Exception as e:
            print(e)

    def load_model(self):
        try:
            file_path = QtWidgets.QFileDialog.getOpenFileName()[0]

            self.model = Word2Vec.load(file_path)

            self.lst_vocab.addItems(list(self.model.wv.vocab.keys()))
            self.lbl_vocab_size.setText(f'Vocab size: {len(list(self.model.wv.vocab.keys()))}')

            self.update()

            self.write_to_log(f'model loaded from {file_path}')

        except:
            pass

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
        self.lbl_word.setText('')
        self.txt_embedding.setText('')
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

    def get_time(self):
        # to be used with write_to_log()

        return datetime.now().strftime('%H:%M:%S')
    
    def write_to_log(self, msg, error=False):
        # write info, errors, etc. to the screen

        li = QtWidgets.QListWidgetItem()
        li.setText(f'[{self.get_time()}] {msg}')

        if error:
            li.setForeground(QtGui.QColor(255,0,0))

        self.lst_log.addItem(li)
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
            self.write_to_log('select a word to view snapshots', True)

        except:
            pass

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

        except:
            pass

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
            self.write_to_log('error selecting file', True)

    def handle_manual_input(self):
        if len(self.txt_input.toPlainText()) > 0:
            sentences = [i for x in [x.split('\n') for x in sent_tokenize(self.txt_input.toPlainText())] for i in x]
            sentences = [[x for x in wordpunct_tokenize(' '.join([(contractions[s.lower()] if s.lower() in contractions else s.lower()) for s in sent.split()])) if str.isalnum(x)] for sent in sentences]

            self.add_to_vocab(sentences)

    def show_sim_plot_external(self):
        self.show_sim_plot(embedded=False)
    
    def show_ran_plot_external(self):
        self.show_ran_plot(embedded=False)

    def tabs_bottom_left_changed(self):
        if self.tab_bottom_left.currentIndex() == 0:
            self.show_sim_plot()
        elif self.tab_bottom_left.currentIndex() == 1:
            self.show_ran_plot()

    def clear_input(self):
        self.txt_input.clear()
        
    def add_to_vocab(self, sentences):

        self.write_to_log('adding vocab to model')

        self.chunk_count = int(self.cmb_chunk_count.currentText())

        if len(sentences) < self.chunk_count:
            self.voc.extend(sentences)
            self.model = Word2Vec(self.voc, min_count=1)
            self.model_snapshots.append(self.model)

            self.write_to_log('model created (1 snapshot)')
        
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

            self.write_to_log(f'model created ({self.chunk_count} snapshots)')

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
            word = self.lst_vocab.selectedItems()[0].text()
            self.lbl_word.setText(f"Embedding vector for \"{word}\"")
            self.txt_embedding.setText( str(self.model.wv.get_vector(word)) )

        except Exception as e:
            print(e)

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

        except:
            pass

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

        except:
            pass

    def build_similar_table(self):
        try:
            sim = self.model.wv.most_similar(self.lst_vocab.selectedItems()[0].text(), topn=7)
            self.tbl_similar.setRowCount(len(sim))
            for i,pair in enumerate(sim):
                self.tbl_similar.setItem(i,0,QtWidgets.QTableWidgetItem(pair[0]))
                self.tbl_similar.setItem(i,1,QtWidgets.QTableWidgetItem(str(pair[1])))
        except:
            pass

    def retranslateUi(self, win_main):
        _translate = QtCore.QCoreApplication.translate
        win_main.setWindowTitle(_translate("win_main", "Embedding Explorer"))
        self.btn_search_list.setText(_translate("win_main", "🔎 "))
        self.btn_sort.setText(_translate("win_main", "Sort"))
        self.lbl_selected_word.setText(_translate("win_main", "<html><head/><body><p>Selected word: NONE</p></body></html>"))
        self.lbl_vocab_size.setText(_translate("win_main", "Vocab size: 0"))
        self.tabs_deets.setTabText(self.tabs_deets.indexOf(self.tab_embed), _translate("win_main", "Embeddings"))
        self.tabs_deets.setTabText(self.tabs_deets.indexOf(self.tab_similar), _translate("win_main", "Similar Words"))
        self.label_2.setText(_translate("win_main", "# of Words:"))
        self.cmb_num_sim_plot.setItemText(0, _translate("win_main", "5"))
        self.cmb_num_sim_plot.setItemText(1, _translate("win_main", "10"))
        self.cmb_num_sim_plot.setItemText(2, _translate("win_main", "15"))
        self.cmb_num_sim_plot.setItemText(3, _translate("win_main", "20"))
        self.btn_create_ext_sim_plot.setText(_translate("win_main", "Create External Plot"))
        self.tab_bottom_left.setTabText(self.tab_bottom_left.indexOf(self.tab_chart_one), _translate("win_main", "Similarity Plot"))
        self.label_3.setText(_translate("win_main", "# of Words:"))
        self.cmb_num_ran_plot.setItemText(0, _translate("win_main", "5"))
        self.cmb_num_ran_plot.setItemText(1, _translate("win_main", "10"))
        self.cmb_num_ran_plot.setItemText(2, _translate("win_main", "15"))
        self.cmb_num_ran_plot.setItemText(3, _translate("win_main", "20"))
        self.btn_create_ext_ran_plot.setText(_translate("win_main", "Create External Plot"))
        self.btn_refresh_ran_plot.setText(_translate("win_main", "Refresh"))
        self.tab_bottom_left.setTabText(self.tab_bottom_left.indexOf(self.tab_chart_two), _translate("win_main", "Random Plot"))
        self.btn_load_snapshots.setText(_translate("win_main", "Create Model Snapshots"))
        self.btn_prev_snap.setText(_translate("win_main", "Previous"))
        self.btn_next_snap.setText(_translate("win_main", "Next"))
        self.tab_bottom_left.setTabText(self.tab_bottom_left.indexOf(self.tab_snapshots), _translate("win_main", "Model Snapshots"))
        self.label_5.setText(_translate("win_main", "1st Word:"))
        self.label_6.setText(_translate("win_main", "2nd Word:"))
        self.btn_math_equal.setText(_translate("win_main", "Calculate"))
        self.label_13.setText(_translate("win_main", "PLUS"))
        self.label_15.setText(_translate("win_main", "EQUALS"))
        self.label_8.setText(_translate("win_main", "MINUS"))
        self.label_10.setText(_translate("win_main", "EQUALS"))
        self.tab_bottom_left.setTabText(self.tab_bottom_left.indexOf(self.tab_math), _translate("win_main", "Embedding Math"))
        self.label_7.setText(_translate("win_main", "<html><head/><body><p>Type or paste in text to create embeddings...</p></body></html>"))
        self.btn_add_input.setText(_translate("win_main", "Add"))
        self.btn_clear_input.setText(_translate("win_main", "Clear"))
        self.label_4.setText(_translate("win_main", "<html><head/><body><p>...or load a file</p></body></html>"))
        self.btn_upload_file.setText(_translate("win_main", "Select File"))
        self.tabs_other_options.setTabText(self.tabs_other_options.indexOf(self.tab), _translate("win_main", "Log"))
        self.groupBox.setTitle(_translate("win_main", "Snapshots"))
        self.chk_create_snaps.setToolTip(_translate("win_main", "check it out!"))
        self.chk_create_snaps.setText(_translate("win_main", "Create snapshots"))
        self.label_9.setText(_translate("win_main", "Chunk Count"))
        self.cmb_chunk_count.setCurrentText(_translate("win_main", "1"))
        self.cmb_chunk_count.setItemText(0, _translate("win_main", "1"))
        self.cmb_chunk_count.setItemText(1, _translate("win_main", "3"))
        self.cmb_chunk_count.setItemText(2, _translate("win_main", "5"))
        self.cmb_chunk_count.setItemText(3, _translate("win_main", "7"))
        self.cmb_chunk_count.setItemText(4, _translate("win_main", "10"))
        self.groupBox_2.setTitle(_translate("win_main", "Other"))
        self.btn_reset.setText(_translate("win_main", "Reset Everything"))
        self.groupBox_3.setTitle(_translate("win_main", "Import/Export"))
        self.btn_save_model.setText(_translate("win_main", "Save Model"))
        self.btn_load_model.setText(_translate("win_main", "Load Model"))
        self.tabs_other_options.setTabText(self.tabs_other_options.indexOf(self.tab_options), _translate("win_main", "General Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win_main = QtWidgets.QMainWindow()
    ui = Ui_win_main()
    ui.setupUi(win_main)
    win_main.show()
    sys.exit(app.exec_())