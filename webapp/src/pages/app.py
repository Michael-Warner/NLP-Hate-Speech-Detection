"""Main module for the streamlit app"""

# importing relevant python packages
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_tweet(tweet): # for cleaning the sentence
    tweet = re.sub(r'http\S+', '', tweet) # remove http links
    tweet = re.sub(r'bit.ly/\S+', '', tweet) # rempve bitly links
    tweet = tweet.strip('[link]') # remove [links]
    my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]\\\\\^_`{|}~•@#'
    tweet = re.sub('(RT\s@[A-Za-z0-9-_]+[A-Za-z0-9-_]+)', '', tweet) # remove retweet
    tweet = re.sub('(@[A-Za-z0-9-_]+[A-Za-z0-9-_]+)', '', tweet)
    tweet = tweet.lower() # lower case
    tweet = re.sub('['+my_punctuation + ']+', ' ', tweet) # strip punctuation
    tweet = re.sub('([0-9]+)', '', tweet) # remove numbers
    tweet = re.sub('amp', '', tweet) # remove amp
    tweet = re.sub('\s+', ' ', tweet) #remove double spacing
    return tweet

def write():
    tweet_input = st.beta_container()
    model_results = st.beta_container()
    contact = st.beta_container()

    with tweet_input:
        st.header('Is Your Tweet Considered Hate Speech?')
        user_text = st.text_input('Write the Tweet', max_chars=280) # setting input as user_text


    with model_results:    
        if st.button("Predict"): 
            # removing punctuation
            #user_text = re.sub('[%s]' % re.escape(string.punctuation), '', user_text)
            user_text = clean_tweet(user_text)
            
            # Customizing stop words list
            stop_words = stopwords.words('english')
            newStopWords = ['ur','u','nd'] # new stop word
            remove_stopword = ['not','no','nor',"don","aren","couldn","didn","hadn","hasn","haven","isn","mustn","mightn","needn","shouldn",
                   "wasn","wouldn","won"] # stop words that we don't want
            stop_words.extend(newStopWords) # add new stop word
            stop_words = [OldStopWords for OldStopWords in stop_words if OldStopWords not in remove_stopword] # remove some stop words
            
            # tokenizing
            tokens = nltk.word_tokenize(user_text)
            # removing stop words
            stopwords_removed = [token.lower() for token in tokens if not token.lower() in set(stop_words)]
            # taking root word
            lemmatizer = WordNetLemmatizer() 
            lemmatized_output = []
            for word in stopwords_removed:
                lemmatized_output.append(lemmatizer.lemmatize(word))

            # instantiating count vectorizor
            tfidf = TfidfVectorizer()
            X_train = pickle.load(open('pickle/X_train.pkl', 'rb'))
            X_test = lemmatized_output
            tfidf_data_train = tfidf.fit_transform(X_train)
            tfidf_data_test = tfidf.transform(X_test)

            # loading in model
            final_model = pickle.load(open('pickle/svm_model.pkl', 'rb'))

            # apply model to make predictions
            prediction = final_model.predict(tfidf_data_test[0])

            if prediction == 0:
                st.error('**Hate Speech  :anger:**')
            elif prediction == 1:
                st.warning('**Offensive Language  :collision:**')
            else:
                st.success('**Neither  :smiley:**')
            st.text('')
            



