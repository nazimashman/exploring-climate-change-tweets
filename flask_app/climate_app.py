from flask import Flask, render_template
import numpy as np
from pymongo import MongoClient
import json
import pandas as pd
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.feature_extraction.text import CountVectorizer
from gensim import corpora, models, similarities, matutils
import re
import numpy.ma as ma
from collections import defaultdict

from textblob import TextBlob
import gensim
import pyLDAvis
from pyLDAvis import gensim as gensimvis
import spacy
import pickle


# Initialize the app

app = Flask(__name__)


main_topics = [{'topic':'Climate','link':'/climate'}, {'topic':'Wildlife', 'link':'/wildlife'}]

def get_links(topic):
    with open(topic+".pkl", 'rb') as picklefile:
        topics = pickle.load(picklefile)
    return topics



@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', topics=main_topics)

@app.route("/climate")
def climate():
    for topic in get_links('climate'):
        print(topic)
    return render_template('climate.html', topics = get_links('climate') )

@app.route("/wildlife")
def wildlife():
    return render_template('climate.html', topics = get_links('wildlife') )




if __name__== "__main__":
    app.run(debug=True)
