# sentiment.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Dean Nunis
# Email: nunis@chapman.edu
# Course: CPSC 353
# Assignment: PA03 Sentiment Analysis
# Version 1
# Date: October 19, 2020

# Demonstrates connecting to the twitter API and accessing the twitter stream

import twitter
import sys
import codecs


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

CONSUMER_KEY = 'I0DwZsN8u7LbowL70TcDKUyOx'
CONSUMER_SECRET = '66tvCPVWUPWdoLRilYlIcoQVON9C7KcnHmwyEhpjRY7pw7sbko'
OAUTH_TOKEN = '1312062176375435264-u6Awuu7pDcxaQuX4bVSYpo7JwhFZWp'
OAUTH_TOKEN_SECRET = '18HajgueheJBHQ1nUVVyWbaCubarbmCljRXXe8R1ubvBD'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# user input
input1 = input('Enter a search term: ')
input2 = input('Enter a search term: ')
count = 1000


search_results = twitter_api.search.tweets(q=input1, count=count)
statuses = search_results['statuses']

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError:
        break

    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

    status_texts = [status['text']
                    for status in statuses]

    screen_names = [user_mention['screen_name']
                    for status in statuses
                    for user_mention in status['entities']['user_mentions']]

    hashtags = [hashtag['text']
                for status in statuses
                for hashtag in status['entities']['hashtags']]

    # Compute a collection of all words from all tweets
    words = [w
             for t in status_texts
             for w in t.split()]

    sent_file = open('AFINN-111.txt')
    # initialize an empty dictionary
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        # Convert the score to an integer.
        scores[term] = int(score)
    # Calculate the sentiment score for the word
    score = 0
    for word in words:
        uword = word.encode('utf-8')
        if word in scores.keys():
            score = score + scores[word]

search_results = twitter_api.search.tweets(q=input2, count=count)
statuses = search_results['statuses']

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError:
        break

    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

    status_texts = [status['text']
                    for status in statuses]

    screen_names = [user_mention['screen_name']
                    for status in statuses
                    for user_mention in status['entities']['user_mentions']]

    hashtags = [hashtag['text']
                for status in statuses
                for hashtag in status['entities']['hashtags']]

    # Compute a collection of all words from all tweets
    words = [w
             for t in status_texts
             for w in t.split()]

    sent_file = open('AFINN-111.txt')
    # initialize an empty dictionary
    scores = {}
    for line in sent_file:
        term, score2 = line.split("\t")
        # Convert the score to an integer.
        scores[term] = int(score2)
    # Calculate the sentiment score for the word
    score2 = 0
    for word in words:
        uword = word.encode('utf-8')
        if word in scores.keys():
            score2 = score2 + scores[word]
# checks to see if the first input is greater than the second and vice-versa
if score > score2:
    print(input1, "has a more positive sentiment score than", input2)
else:
    print(input2, "has a more positive sentiment score than", input1)
# prints the sentiment values of inputs
print(input1, "has a sentiment value of", score)
print(input2, "has a sentiment value of", score2)
