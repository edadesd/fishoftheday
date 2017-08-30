#!/usr/bin/python

import random
import tweepy

from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes

REPLY_LIMIT = 160
VOWELS = ("A", "E", "I", "O", "U")

def rollFish():
    generatedFish = random.choice(fishes)
    fishName = generatedFish['name']
    if fishName[0] in VOWELS:
        fullCatch = "an " + fishName
    elif fishName[0:3] == "The":
        fullCatch = fishName
    else:
        fullCatch = "a " + fishName

    if ("Timeworn" in fishName or "Spoil" in fishName or "Magic Bucket" in fishName or
        "Tiny Tatsunoko" in fishName or "Castaway Chocobo Chick" in fishName or
        "Gigantpole" in fishName or "Tiny Tortoise" in fishName):
        fishLength = generatedFish['max']
    else:
        roll = random.randint(1, 100)
        if roll >= 85:
            fishLength = round((float(roll)/100.0) * generatedFish['max'], 1)
            fullCatch += " (HQ)"
        else:
            sizeMod = float(random.randint(50, 84))
            fishLength = round((sizeMod/100.0) * generatedFish['max'], 1)

    fishString = "You land " + fullCatch + " measuring " + str(fishLength) + " ilms!\n"
    fishString = fishString

    return fishString


random.seed()

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

repliedUsers = []

with open("/home/pi/everyFish/latestMention.txt", "r") as tracking:
    txt = tracking.readline()
    latestMentionStr = txt.strip()
    latestMention = int(latestMentionStr)
    newLatestMention = latestMention

with open("/home/pi/everyFish/windowReplies.txt", "r") as tracking: 
    txt = tracking.readline()
    windowRepliesStr = txt.strip()
    windowReplies = int(windowRepliesStr)

mentions = api.mentions_timeline(str(latestMention))

for mention in mentions:
    if mention.id > latestMention:
        if mention.id > newLatestMention:
            newLatestMention = mention.id
        if mention.author.id not in repliedUsers:
            repliedUsers.append(mention.author.id)
            if "fish" in mention.text or "Fish" in mention.text:
                if windowReplies < REPLY_LIMIT:                        
                    screenName = "@" + mention.author.screen_name + " "
                    postString = screenName + rollFish()
                    try:
                        api.update_status(postString, mention.id)
                        windowReplies += 1
                        print postString
                    except:
                        continue
        else:
            continue

with open("/home/pi/everyFish/latestMention.txt", "w") as tracking:
    tracking.write(str(newLatestMention))
with open("/home/pi/everyFish/windowReplies.txt", "w") as tracking:
    tracking.write(str(windowReplies))                        
        
        


