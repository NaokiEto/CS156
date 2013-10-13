import random
import numpy as np

listIter = range(1000)

misclassified = 0

outofsample = 0

numPoints = 6

for num in range(1000):

    # coordinates for line
    a1 = random.random()*2.0 - 1.0
    a2 = random.random()*2.0 - 1.0 

    b1 = random.random()*2.0 - 1.0
    b2 = random.random()*2.0 - 1.0

    slope = (b2 - b1) / (a2 - a1)

    x = [0]*numPoints
    y = [0]*numPoints

    # y-coordinates of random data
    ydat = [0]*numPoints

    # signs
    ysig = [0]*numPoints

    for i in range(numPoints):

        # x-coordinates
        x[i] = random.random()*2.0 - 1.0

        # y-coordinates of the target function
        y[i] = slope*(x[i] - a1) + b1

        # y-coordinates of random data
        ydat[i] = random.random()*2.0 - 1.0
        if (ydat[i] > y[i]):
            ysig[i] = 1
        else:
            ysig[i] = -1

    ysignTarg = np.zeros((numPoints, 1))
    xCoords = np.zeros((numPoints, 3))    

    for j in range(numPoints):
        ysignTarg[j, 0] = float(ysig[j])
        xCoords[j, 0] = 1
        xCoords[j, 1] = float(x[j])
        xCoords[j, 2] = float(ydat[j])

    # Calculate the pseudo inverse
    pseudoInv = np.dot(np.linalg.inv(np.dot(np.transpose(xCoords), xCoords)), np.transpose(xCoords))

    weights = np.dot(pseudoInv, ysignTarg)

    w0 = weights[0]
    w1 = weights[1]
    w2 = weights[2]

    numIter = 0
    done = 1

    while(done > 0):
        i = 0

        x0 = 1
        x1 = x[i]
        x2 = ydat[i]

        ynval = w0*x0 + w1*x1 + w2*x2

        if(ynval > 0):
            ysigN = 1
        else:
            ysigN = -1

        # the coordinates of missed points
        misList = []

        # the signs
        tList = []

        # figure out if each point is classified or misclassfied
        # if misclassified, correct w

        # get the misclassfied points
        while(i < numPoints - 1):
            i+=1
            x1 = x[i]
            x2 = ydat[i]

            ynval = w0*x0 + w1*x1 + w2*x2

            if(ynval > 0):
                ysigN = 1
            else:
                ysigN = -1

            if (ysigN != ysig[i]):
                misList.append(i)
                tList.append(ysig[i])

        lastElem = len(misList) - 1

        if (lastElem != -1):
            randIndex = random.randint(0, lastElem)
            w0 += tList[randIndex]*1
            w1 += tList[randIndex]*x[misList[randIndex]]
            w2 += tList[randIndex]*ydat[misList[randIndex]]
            numIter+=1
        else:
            done = 0
                                                                                                                                                
    listIter[num] = numIter

total = 0
for term in range(1000):
    total += listIter[term]

average = total/1000.0

print total
print average
