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

validFish = []
for fish in fishes:
        if fish['available'] == "True":
                validFish.append(fish)

fotd = validfish.choice()


postString = "Fish of the Day: " + "\n" + fotd['name']+ "\n" + fotd['url']
print postString

api.update_status(postString)

with open(filename, "w") as fishleft:
	for i in remainingIndices:
		if i != chosen:
	        	fishleft.write(i)
