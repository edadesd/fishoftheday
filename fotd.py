#!/usr/bin/python

import tweepy
import random
import os
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes

random.seed()

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

filename = "/home/pi/everyFish/fishleft.txt"

with open(filename, "r") as fishleft:
    remainingIndices = fishleft.readlines()

chosen = random.choice(remainingIndices)
chosenStripped = chosen.rstrip("\n")
fotdIndex = int(chosenStripped)


fotdName = fishes[fotdIndex]['name']
fotdUrl = fishes[fotdIndex]['url']

postString = "Fish of the Day: " + "\n" + fotdName + "\n" + fotdUrl
print postString

api.update_status(postString)

with open(filename, "w") as fishleft:
	for i in remainingIndices:
		if i != chosen:
	        	fishleft.write(i)
