#other half of rin: find trends in data
import pickle
import sys

fileName = "train.rin"
dataFileName = "data"

#load array from file
def loadArray():
    return pickle.load(open(fileName, "rb"))

#load # of times run from file
def loadData():
    return pickle.load(open(dataFileName, "rb"))

#do a pretty print of the data
arr = loadArray()
for idx, x in enumerate(arr):
    for idx2, y in enumerate(x):
        if(idx == idx2):
            sys.stdout.write("x.x ")
        else:
            sys.stdout.write(str(y) + " ")
    sys.stdout.write("\n")

#find smallest # in grid on one half
smallestVal = arr[0][0]
smallestX = 0
smallestY = 0

for idx, x in enumerate(arr):
    for idx2, y in enumerate(x[0:idx]):
        if y < smallestVal:
            smallestVal = y
            smallestX = idx2
            smallestY = idx

#make new array with combined numbers 
