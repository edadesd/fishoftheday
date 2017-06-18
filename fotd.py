#!/usr/bin/python

import tweepy
import random
import os
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes

random.seed()

#Authenticate and setup tweepy API object

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#Change this to the path to your fishleft.txt file
filename = "/home/everyFish/fishleft.txt"

''' Read the fishleft file line by line
and choose a random fish to post.'''

with open(filename, "r") as fishleft:
    remainingIndices = fishleft.readlines()

chosen = random.choice(remainingIndices)
chosenStripped = chosen.rstrip("\n")
fotdIndex = int(chosenStripped)

'''Take the fish's
name and url entries from the chosen fish's
dict.'''

fotdName = fishes[fotdIndex]['name']
fotdUrl = fishes[fotdIndex]['url']

#Format the post and send it.

postString = "Fish of the Day: " + "\n" + fotdName + "\n" + fotdUrl
print postString

api.update_status(postString)

'''Write all of the indices back to fishleft
except for the one that was chosen. This has
the effect of removing the chosen index from the
file so it will not be repeated on later executions.'''

with open(filename, "w") as fishleft:
	for i in remainingIndices:
		if i != chosen:
	        	fishleft.write(i)
