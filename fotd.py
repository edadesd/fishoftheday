#!/usr/bin/python

import tweepy
import random
import json
import os
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes


fishfile = "/home/pi/everyFish/fishes.py"

random.seed()

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

validFish = []
for fish in fishes:
        if fish['available'] == "True":
                validFish.append(fish)

fotd = random.choice(validFish)
fotdIndex = fotd['index']

postString = "Fish of the Day: " + "\n" + fotd['name']+ "\n" + fotd['url']
# print postString

api.update_status(postString)

fishes[fotdIndex]['available'] = "False"
# print fishes[fotdIndex]

with open(fishfile, "w") as fishFile:
        fishFile.write("fishes = [\n")
        index = 0
        for fish in fishes:
                fishString = json.dumps(fish)
                if index < len(fishes) - 1:
                        fishString += ",\n"
                else:
                        fishString += "\n"
                fishFile.write(fishString)
                index += 1
        fishFile.write("]")
