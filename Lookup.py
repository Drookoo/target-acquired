from TwitterSearch import *
import json, plotly
import plotly.plotly as py
import time
from plotly.graph_objs import *

# Future: Graphs, compare two users

negativelist = ['dumb', 'stupid', 'pig', 'crooked', 'lyin', 'weak', 'loser', 'moron', 'fraud', 'ass', 'trash', 'crybaby'];

positivelist = ['happiness', 'joy', 'compassion', 'respect', 'accept', 'able', 'kindness',];

final = [];

goodwords = 0
badwords = 0

result = input("Who would you like to look up? Enter the Twitter handle of the individual without the '@' ")

try:
    tuo = TwitterUserOrder(str(result))

    ts = TwitterSearch(
        consumer_key = "KkpFEpTqGFRjomRBIjM8JnY6o",
        consumer_secret = "sVVTUbyDjx20UTYZxHrJqzeTWs1Z4lLxWWjyvpOTHqXLlKfttK",
        access_token = "361562432-BFrbbe5dmlmf3HaaeMOIdqP8XUxzxNmf9p5JYZpq",
        access_token_secret = "265EGC3annnj9KuyuFMVd96KYJUIp4g7moeO48KDsG1pg"
    )
    for tweet in ts.search_tweets_iterable(tuo):
        words = (str(tweet['text'].encode("ascii", "ignore"))).split(" ")
        print(words)
        final.extend(words)
except TwitterSearchException as e: # catch all those ugly errors
    print(e)

print(final)

#writes into a file
with open('tweets.txt', 'w') as outfile:
    json.dump(final, outfile)

print("The number of words is: " + str(len(final)))

for negativeword in negativelist:
    print("The word %s" % negativeword + " occurs: " + str(final.count(negativeword)) + " times")
    badwords = badwords + final.count(negativeword)

for positiveword in positivelist:
    print("The word %s" % positiveword + " occurs: " + str(final.count(positiveword)) + " times")
    goodwords = goodwords + final.count(positiveword)

if negativeword > positiveword:
    print("The user @" + result + " is a negative individual")
elif negativeword < positiveword:
    print("The user @" + result + " is a positive individual")
else:
    print("the user @" + result + " is equally positive and negative")

#graphing
plotly.tools.set_credentials_file(
    username='nachozombie',
    api_key='ajvmmn1scx'
)

print("We have " + str(goodwords) + " words of encouragement")
print("We have " + str(badwords) + " words of toxicity")

fig = {
    'data': [{'labels': ['Positive Words', 'Negative Words'],
              'values': [goodwords, badwords],
              'type': 'pie'}],
    'layout': {'title': 'Your user data visualized'}
     }

time.sleep(10)
py.plot(fig)