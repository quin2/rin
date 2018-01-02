#other half of rin: find trends in data
import pickle
import sys

fileName = "train.rin"
dataFileName = "data"

print("hello rin")
print()

#load array from file
def loadArray():
    return pickle.load(open(fileName, "rb"))

#load # of times run from file
def loadData():
    return pickle.load(open(dataFileName, "rb"))

def sim(member1, member2, outside):
    return

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

#do a pretty print of the data
arr = loadArray()

#define nodes
nodesX = []
nodesY = []
for idx, x in enumerate(arr):
    nodesX.append([idx])
    nodesY.append([idx])

debugPrint(arr, nodesX, nodesY)
print()

smallestVal = arr[1][0]
smallestX = 0
smallestY = 1
merges = []

cycleCount = 0
cycleMax = 6

while cycleCount < cycleMax:
    #find smallest # in grid on one half
    for idx, x in enumerate(arr):
        for idx2, y in enumerate(x[0:idx]):
            if y < smallestVal:
                smallestVal = y
                smallestX = idx2
                smallestY = idx

    print("smallest value index is")
    sys.stdout.write(str(nodesX[smallestX]) + " " + str(nodesY[smallestY]) + "\n")
    print()

    #append smallest value to merge list
    merges.append(nodesX[smallestX] + nodesY[smallestY])
    print(merges)
    print()

    #merge onto old col, delete the old one
    nodesX[smallestX] = nodesX[smallestX] + nodesY[smallestY]
    nodesY[smallestX] = nodesY[smallestX] + nodesY[smallestY]

    #only need to step through arr once to compare
    #not 100% sure this isright
    for idx, x in enumerate(arr):
        if arr[smallestX][idx] < arr[smallestY][idx]:
            x[smallestX] = arr[smallestX][idx]
            arr[idx][smallestX] = arr[smallestX][idx]
        else:
            x[smallestX] = arr[smallestY][idx]
            arr[idx][smallestX] = arr[smallestX][idx]

    #delate r/c in list
    del arr[smallestY]

    for x in arr:
        del x[smallestX]

    del nodesY[smallestY]
    del nodesX[smallestY]

    debugPrint(arr, nodesX, nodesY)
    print()

    cycleCount += 1
