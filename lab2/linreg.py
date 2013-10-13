import random
import numpy as np

misclassified = 0

outofsample = 0

numPoints = 100

numPointsMonte = 1000

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

    # calculate the weights
    w0 = weights[0]
    w1 = weights[1]
    w2 = weights[2]

    for i in range(numPoints):
        x0 = 1
        x1 = x[i]
        x2 = ydat[i]

        ynval = w0*x0 + w1*x1 + w2*x2

        if(ynval > 0):
            ysigN = 1
        else:
            ysigN = -1

        if (ysigN != ysig[i]):
            misclassified += 1

    # Monte Carlo simulation
    x2 = range(numPointsMonte)
    y2 = range(numPointsMonte)

    # y-coordinates of random data
    ydat2 = range(numPointsMonte)

    # y-coordinates of hypothesis
    yhypo2 = range(numPointsMonte)

    # signs for target
    ysig2 = range(numPointsMonte)

    # signs for hypothesis
    ysigHypo2 = range(numPointsMonte)

    for i in range(numPointsMonte):
        x2[i] = random.random()*2.0 - 1.0

        y2[i] = slope*(x2[i] - a1) + b1
        ydat2[i] = random.random()*2.0 - 1.0
        yhypo2[i] = w0*1 + w1*x2[i] + w2*ydat2[i]
        
        if (ydat2[i] < y2[i]):
            ysig2[i] = -1
        else:
            ysig2[i] = 1

        if(yhypo2[i] > 0):
            ysigHypo2[i] = 1

        else:
            ysigHypo2[i] = -1

        if(ysig2[i] != ysigHypo2[i]):
            outofsample += 1

print "the number of misclassified out of sample points are: ", outofsample

print "the number of misclassified points is: ", misclassified


