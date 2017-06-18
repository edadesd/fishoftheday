'''Resets the tracked number of replies
stored in windowReplies.txt to zero to indicate
the start of a new fifteen minute window.'''


filename = "/home/everyFish/windowReplies.txt"

with open(filename, "w") as resetFile:
    resetFile.write("0")
