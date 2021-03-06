#!/usr/bin/python

import tweepy
import random
from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes

fishfile = "/home/pi/everyFish/fishes.py"

random.seed()

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Make a list of fish that have not already been posted
# by iterating through the list of fish and extracting
# the ones that have not been already.

validFish = [fish for fish in fishes if fish['available']]

# Choose a fish from the available fish and post its contents.

fotd = random.choice(validFish)
fotdIndex = fotd['index']

postString = "Fish of the Day: " + "\n" + fotd['name'] 
# print postString

api.update_status(postString)

# Update the chosen fish to indicate it has already been posted.

fishes[fotdIndex]['available'] = False
# print fishes[fotdIndex]

# Write each of the fish into the file by dumping its dict as a string.

with open(fishfile, "w") as fishFile:
        fishFile.write("fishes = [\n")
        index = 0
        for fish in fishes:
                fishString = str(fish)
                if index < len(fishes) - 1:
                        fishString += ",\n"
                else:
                        fishString += "\n"
                fishFile.write(fishString)
                index += 1
        fishFile.write("]")
