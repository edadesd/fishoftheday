# fishoftheday
(Python 2.7) Posts an item from a list once per day and replies to mentions with an item from the list.

Enter the item information in fishes.py and enter each the index of each item on its own line in fishleft.txt.

You will need to register the bot as a Twitter app to get the necessary values for secret.py. See the included secret.py for the names of the values you will need to include, then copy them from your app page to secret.py as the values for the listed variables so the bot can use them to authenticate. This enables posting the code without giving away your credentials - just remember to never expose your secret.py file!

Start the bot by scheduling regular execution of fotd.py once a day to get the daily item posted. To get the reply functionality working, schedule execution of runfish.sh every minute and resetWindow.py every 15 minutes. Setting these up via UNIX crontab is demonstrated in the crontab file. Be sure to change the filepaths as appropriate.
