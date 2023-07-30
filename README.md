# Spam Filter

The Spam Filter is a project that utilizes a machine learning model built by stacking hyptertuned Logistic Regression, MultinominalNB, Support Vector Machine Classification and Decision Tree models. It provides and API endpoint to generate a response classifying input text as spam or not spam. This project leverages customtkinter to create an interactive GUI that allows text to be inputted and displays the classification of the email text in realtime. 

## How It Works

### Model production (filter_model_creation.ipynb)

The core functionality of classifying spam or not spam emails is implemented in `filter_model_creation.ipynb`. The file uses a spam email dataset found at https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv to train a supervised model that is 97.5% accurate in classifying spam emails. 

In order to to generate predictions using the machine learning model created, `stack_model.pickle` and `columns.json` are exported with the machine learning model and dataframe columns necessary for model prediction stored in their respective files.   

## Inside(spamFilter.zip)

### GUI Spam Filter(Gui.py)

The visual spam filter application is implemented directly in `Gui.py` which leverages customtkinter to accomplish a few tasks:

1. Load machine learning model stored in `stack_model.pickle` as well as data columns in `columns.json` 
2. Grab variable user email text from the GUI 
3. Tokenize text input by grouping input text which has been split into a list of lowercase words into a numpy array, modelling the dataframe columns used to train `stack_model.pickle`.
4. Return a spam or not spam classification to the GUI through altering label text as well as fg_color and text_color based on response. 


