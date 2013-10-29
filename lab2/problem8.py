import random
import numpy as np

misclassified = 0

outofsample = 0

numPoints = 1000

for num in range(1000):

    x = [0]*numPoints

    # y-coordinates of random data
    ydat = [0]*numPoints

    # signs
    ysig = [0]*numPoints

    nonoise = [0]*numPoints

    for i in range(numPoints):

        # x-coordinates
        x[i] = random.random()*2.0 - 1.0

        # y-coordinates of random data
        ydat[i] = random.random()*2.0 - 1.0
	
	# figure out the sign
        if (x[i]**2 + ydat[i]**2 - 0.6 > 0):
            nonoise[i] = 1
            ysig[i] = 1
        else:
            nonoise[i] = -1
            ysig[i] = -1

    for i in range(int(numPoints*0.1)):
        ysig[i] = ysig[i]*-1

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
print "the number of misclassified points is: ", misclassified


