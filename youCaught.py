#!/usr/bin/python

import random
import tweepy

from secret import CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fishes import fishes

REPLY_LIMIT = 160
VOWELS = ("A", "E", "I", "O", "U")

'''Chooses an entry from the list of fish and formats
the information from that entry as a string ready to post
to Twitter. Determines a random length based on that fish's
maximum length.'''

def rollFish():
    '''Choose an entry from the full list at random and
    retrieve its name.'''
    generatedFish = random.choice(fishes)
    fishName = generatedFish['name']
    
    '''Add "a" or "an" to the front of the fish
    name if appropriate to make the fish a (grammatical) direct
    object in the post.'''
    if fishName[0] in VOWELS:
        fullCatch = "an " + fishName
    elif fishName[0:3] == "The":
        fullCatch = fishName
    else:
        fullCatch = "a " + fishName

    '''Determine the fishs's length via random roll.'''
        
    #Timeworn Maps and Sky Pirate Spoils do not have variable lengths.
    if "Timeworn" in fishName or "Spoil" in fishName:
        fishLength = generatedFish['max']
    else:
        #Rolls from 1-100, inclusive.
        roll = random.randint(1, 100)
        
         '''There is a 15% chance of the fish being High Quality (HQ). If the fish
        is HQ, its length is roll / max which produces a result of 85-100% of the
        listed maximum length in fishes.py. Its name gets '(HQ)' appended before posting.'''
        if roll >= 85:
            fishLength = round((float(roll)/100.0) * generatedFish['max'], 1)
            fullCatch += " (HQ)"
            
        '''There is an 85% chance of the fish not being High Quality. fish that are not
        HQ, give it a random length that is 50-84% of the listed maximum length in fishes.py.'''
        
        else:
            sizeMod = float(random.randint(50, 84))
            fishLength = round((sizeMod/100.0) * generatedFish['max'], 1)

            
    '''Build the text of the post as a string based on the results (i.e. fish name and length)
    determined above.'''
    
    fishString = "You land " + fullCatch + " measuring " + str(fishLength) + " ilms!\n"
    fishString = fishString + "\n" + generatedFish['url']

    return fishString


random.seed()

'''Authenticate and create the API object.'''

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

repliedUsers = []

'''Read the status ID number stored in latestMention.txt. 
Every mention retrieved in this execution will be compared to it
to determine if the mention is newer or older.'''

with open("/home/everyFish/latestMention.txt", "r") as tracking:
    txt = tracking.readline()
    latestMentionStr = txt.strip()
    latestMention = int(latestMentionStr)
    newLatestMention = latestMention
    
'''Read how many replies have already been sent out in this 
fifteen minute window. The bot will not send out more replies
if has already reached or exceeded the window limit.'''

with open("/home/everyFish/windowReplies.txt", "r") as tracking: 
    txt = tracking.readline()
    windowRepliesStr = txt.strip()
    windowReplies = int(windowRepliesStr)

'''Get the latest batch of mentions from Twitter and process
them.'''

mentions = api.mentions_timeline(str(latestMention))

for mention in mentions:
    
    '''Discard any mentions older than the recorded
    latest mention. Keep track of the latest mention
    out of all of the mentions.'''
    
    if mention.id > latestMention:
        if mention.id > newLatestMention:
            newLatestMention = mention.id
            
        '''Keep track of each user who has sent a mention
        during this execution. Only reply to one mention
        per author in each execution.'''
        if mention.author.id not in repliedUsers:
            repliedUsers.append(mention.author.id)
            
            '''Only reply if the mention contains "fish"
            to avoid getting an infinite loop of replying to another 
            bot that replies to all messages. The bot's Twitter profile
            tells users who want a reply from the bot to use this word.'''
            if "fish" in mention.text:
                if windowReplies < REPLY_LIMIT:                        
                    '''Format the reply post.'''
                    screenName = "@" + mention.author.screen_name + " "
                    postString = screenName + rollFish()
                    
                    #Attempt to post the reply.
                    try:
                        api.update_status(postString, mention.id)
                        #Increment the number of replies in the current window.
                        windowReplies = windowReplies + 1
                        print postString
                    except:
                        continue
        else:
            continue

            
'''Update the text files containing the latest mention's status ID number
and the number of replies in the current window.'''
with open("/home/everyFish/latestMention.txt", "w") as tracking:
    tracking.write(str(newLatestMention))
with open("/home/everyFish/windowReplies.txt", "w") as tracking:
    tracking.write(str(windowReplies))                        
        
        


