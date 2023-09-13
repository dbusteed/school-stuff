# ECON 484 PROJECT

## Quickstart

If you are just here to run the code and check things out, then all you really need to do is run `model_evaluation.ipynb` found in `python/` folder (or just click [here](python/model_evaluation.ipynb))

The data you need (`processed_tweets.json`) should be in the `data/` folder, so you shouldn't need to worry about building the dataset, etc.

## Other

If you want to mess around with stuff, this is the contents of this directory:

* `python/`
    * all the Python scripts and Notebooks used in data collection and machine learning
    * `get_tweets.py`
        * grabs tweets --> `data/`
        * checkout the comments in-file
        * need to add API keys to `example_secret_config.py`
    * `txt_to_json.py`
        * converts dem txt files to json
    * `feature_extraction.py`
        * extracts features from tweets
        * creates new json
    * `model_evaluation.ipynb`
        * where the machine learning happens
* `data/`
    * data files
    * `*.txt`
        * files for storing each country's tweets
    * `country_tweets.json`
        * output of `txt_to_json.py`
    * `processed_tweets.json`
        * output of `feature_extraction.py`
* `mallet/`
    * stuff for working with MALLET
    * `readme.md`
    * `twitter.mallet`
        * data file need to run MALLET machine learning
    * `mallet_models.ps1`
        * a very rough MALLET script, basically notes so i don't forget what i did