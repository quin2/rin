#todo: find out how to make dictionary, 2D list!! or just preload everything smhhhh
import sys
import random

print("hello rin")

emotions = [
  "anger",
  "annoyance",
  "contempt",
  "disgust",
  "irritation",
  "anxiety",
  "embarrassment",
  "fear",
  "helplessness",
  "powerlessness",
  "worry",
  "doubt",
  "envy",
  "frustration",
  "guilt",
  "shame ",
  "boredom",
  "despair",
  "disappointment",
  "hurt",
  "sadness",
  "shock",
  "stress",
  "tension",
  "amusement",
  "delight",
  "elation",
  "excitement",
  "happiness",
  "joy",
  "pleasure",
  "affection",
  "empathy",
  "friendliness",
  "love",
  "courage",
  "hope",
  "pride",
  "satisfaction",
  "trust",
  "calm",
  "content",
  "relaxed",
  "relieved",
  "serene",
  "interest",
  "politeness",
  "surprise",
  ]

targetLinkages = 3

fileName = "train.rin"

#get input character from console
def getInput():
    dec = input("answer [y/x/n]: ")

    if dec != 'y' and dec != 'x' and dec != 'n':
        getInput()

    return dec


#get and load all the input right here
randValues = []
links = []
linkValues = []

while len(links) < targetLinkages:
    #find new random number each time
    rand = random.randrange(len(emotions))
    y = 0;
    while(y < len(randValues)):
        if(randValues[y] == rand):
            rand = random.randrange(len(emotions))
            y = 0;
        else:
            y += 1;

    randValues.append(rand)

    #map inputted values to array, eventually to be transcribed to master array
    print("")
    print("are you feeling " + emotions[rand] + "?")
    y = getInput()

    if(y == 'y'):
        links.append(rand)
        linkValues.append(1.0)

    elif(y =='x'):
        links.append(rand)
        linkValues.append(0.5)

#move information to master array
for idx, item in enumerate(links):
    for item2 in links[idx + 1:]:
        print(item)
        print(item2)
        print()
