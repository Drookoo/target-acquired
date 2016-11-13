from TwitterSearch import *
import json

wordlist = ['dumb', 'stupid', 'pig', 'crooked', 'lyin', 'weak', 'loser', 'moron', 'fraud', 'ass', 'trash', 'crybaby'];

final = [];

result = input("Who would you like to look up? ")

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

with open('tweets.txt', 'w') as outfile:
    json.dump(final, outfile)

print("The number of words is: " + str(len(final)))

for word in wordlist:
    print("The word %s" % word + " occurs: " + str(final.count(word)) + "times")