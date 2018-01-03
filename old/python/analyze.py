#other half of rin: find trends in data
#kmow when to stop running evo algoritham?
#add better tracing, etc...
import pickle
import sys

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

fileName = "train.rin"
dataFileName = "data"

clusterMax = 5; #target # of clusters

print("hello rin")
print()

#load array from file
def loadArray():
    return pickle.load(open(fileName, "rb"))

#load # of times run from file
def loadData():
    return pickle.load(open(dataFileName, "rb"))

#central printing function
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


#load all data
arr = loadArray()

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

while len(nodesX) > clusterMax: #stop after # of clusters have formed
    #possibly make this when entered emotions are clustered? 
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
