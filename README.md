# fishoftheday
(Python 2.7) Posts an item from a list once per day and replies to mentions with an item from the list. Depends upon the tweepy library: https://github.com/tweepy/tweepy

Enter the item information in fishes.py in python dict format. This is adaptable to whatever purpose you like, so change the name/url to whatever attributes you would like, add attributes, or even remove attributes. The 'seen' attribute tracks whether the bot has already posted a particular item. If you want items to repeat, make sure fotd.py doesn't change the 'available' attribute for anything to 'False'.

You will need to register the bot as a Twitter app to get the necessary values for secret.py. See the included secret.py for the names of the values you will need to include, then copy them from your app page to secret.py as the values for the listed variables so the bot can use them to authenticate. This enables posting the code without giving away your credentials - just remember to never expose your secret.py file!

Start the bot by scheduling regular execution of fotd.py once a day to get the daily item posted. To get the reply functionality working, schedule execution of runfish.sh every minute and resetWindow.py every 15 minutes. Setting these up via UNIX crontab is demonstrated in the crontab file. Be sure to change the filepaths as appropriate.

TODO: Convert project to SQLite database rather than module file containing Python dictionaries.
