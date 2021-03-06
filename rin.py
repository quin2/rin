#quinn v 2018
import sys
import random
import pickle
from pathlib import Path

print("hello rin")

#stores list of all possible emotions
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
  "shame",
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
  ]

fileName = "train.rin" #path for distance matrix
dataFileName = "data" #path for number w/ number of training
linksFileName = "linkages" #path for linkage matrix storage

#get input character from console
def getInput():
    dec = input("answer [y/x/n]: ")

    if dec != 'y' and dec != 'x' and dec != 'n':
        getInput()

    return dec

#menu handling function for main menu
def rinMenu():
    print()
    print("(1) train rin")
    print("(2) cluster emotions")
    print("(3) activate model")
    print("(4) quit")
    menuIn = input("select option > ")

    if menuIn != '1' and menuIn != '2' and menuIn != '3' and menuIn != '4':
        rinMenu()

    if menuIn == '1':
        train()
        rinMenu()

    if menuIn == '2':
        cluster()
        rinMenu()

    if menuIn == '3':
        enable()
        rinMenu()

    return

#create blank array for filling on first run of rin
def createArray():
    toReturn = []
    for emotion in range(len(emotions)): toReturn +=[[0.0] * len(emotions)]
    return toReturn

#universal load function
def load(fName):
    return pickle.load(open(fName, "rb"))

#universal save function
def save(toSave, fName):
    pickle.dump(toSave, open(fName, "wb"))
    return

#central printing function, adapt to work without x and y axies?
def debugPrint(array, xList, yList):
    sys.stdout.write("   ")
    for i in xList:
        sys.stdout.write(str(i))
    sys.stdout.write("\n")

    for idx, x in enumerate(array):
        sys.stdout.write(str(yList[idx]))
        for idx2, y in enumerate(x):
            if(idx == idx2):
                sys.stdout.write("x.x ")
            else:
                sys.stdout.write(str(y) + " ")
        sys.stdout.write("\n")
    print()

#gets input to train matrix
targetLinkages = 5 #target number of yes answers
def train():
    #get and load all the input right here
    randValues = []
    links = []
    linkValues = []
    yesValues = []

    while len(yesValues) < targetLinkages:
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
            yesValues.append(rand)

        elif(y == 'n'):
            links.append(rand)
            linkValues.append(1.0)

        elif(y =='x'):
            links.append(rand)
            linkValues.append(0.5)

    #load data from past sessions
    if not Path(fileName).is_file():
        save(createArray(), fileName)

    emotionData = load(fileName)
    currentNum = load(dataFileName) + targetLinkages

    #move session into master
    for idx, noVal in enumerate(links):
        for yesVal in yesValues:
            emotionData[noVal][yesVal] += linkValues[idx]
            emotionData[yesVal][noVal] += linkValues[idx]

    #save data to array
    save(emotionData, fileName)

    if not Path(dataFileName).is_file():
        save(0, dataFileName)
    else
        save(currentNum, dataFileName)
    return

#clusters all emotions from distance matrix using hierarchical clustering
clusterMax = 5; #target # of clusters
def cluster():
    #load all data
    arr = load(fileName)

    cycleMax = len(arr) - 1

    #define nodes
    nodesX = []
    nodesY = []
    for idx, x in enumerate(arr):
        nodesX.append([idx])
        nodesY.append([idx])

    debugPrint(arr, nodesX, nodesY)
    print()

    smallestVal = arr[1][0]
    linkX = 0
    linkY = 1
    merges = []

    while len(nodesX) > clusterMax: #stop after target # of clusters have formed

        #find smallest # in grid on one half
        smallestVal = arr[1][0]
        linkX = 0
        linkY = 1

        for idx, x in enumerate(arr):
            for idx2, y in enumerate(x[0:idx]):
                if y < smallestVal:
                    smallestVal = y
                    linkX = idx2
                    linkY = idx

        print("smallest value index is")
        sys.stdout.write(str(nodesX[linkX]) + " " + str(nodesY[linkY]) + " " + str(smallestVal) + "\n")
        print()

        #append smallest value to merge list
        merges.append(nodesX[linkX] + nodesY[linkY])
        print(merges)
        print()

        #steps through and adds new distance values to merged columns
        #uses complete-link clustering
        for idx, x in enumerate(arr):
            if x[linkX] > x[linkY]:
                arr[linkX][idx] = x[linkX]
            else:
                x[linkX] = x[linkY]
                arr[linkX][idx] = x[linkY]

        #merge nodes list together
        nodesX[linkX] = nodesX[linkX] + nodesY[linkY]
        nodesY[linkX] = nodesY[linkX] + nodesY[linkY]

        #delate other row and column in distance matrix
        del arr[linkY]

        for x in arr:
            del x[linkY]

        del nodesY[linkY]
        del nodesX[linkY]

        debugPrint(arr, nodesX, nodesY)
        print()

    #print associations
    for x in nodesX:
        print()
        for emotion in x:
            print(emotions[emotion])

    #save associations to file
    save(nodesX, linksFileName)
    return

#use model with emotional input
def enable():
    cluster()

    randValues = []
    feel = ''
    rand = 0

    while feel != 'y':
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
        feel = getInput()

    link = load(linksFileName)
    #search for feel in loadLinkages, find similar emotions
    clusterIndex = 0
    for cluster in link:
        if cluster.count(rand) != 0:
            clusterIndex = cluster

    print("you must also feel:")
    for x in clusterIndex:
        print(emotions[x])
    return

#core handling function
rinMenu()
