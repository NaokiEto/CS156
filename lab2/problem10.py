import random
import numpy as np

misclassified = 0

outofsample = 0

numPoints = 500

numPointsMonte = 300

for num in range(1000):

    x = [0]*numPoints

    # y-coordinates of random data
    ydat = [0]*numPoints

    # signs
    ysig = [0]*numPoints

    for i in range(numPoints):

        # x-coordinates
        x[i] = random.random()*2.0 - 1.0

        # y-coordinates of random data
        ydat[i] = random.random()*2.0 - 1.0
	
        # figure out the sign
        if (x[i]**2 + ydat[i]**2 - 0.6 > 0):
            ysig[i] = 1
        else:
            ysig[i] = -1

    for i in range(int(numPoints*0.1)):
        ysig[i] = ysig[i]*-1

    ysignTarg = np.zeros((numPoints, 1))
    xCoords = np.zeros((numPoints, 6))    

    for j in range(numPoints):
        ysignTarg[j, 0] = float(ysig[j])
        xCoords[j, 0] = 1
        xCoords[j, 1] = float(x[j])
        xCoords[j, 2] = float(ydat[j])
        xCoords[j, 3] = float(x[j]*ydat[j])
        xCoords[j, 4] = float(x[j]**2)
        xCoords[j, 5] = float(ydat[j]**2)

    # Calculate the pseudo inverse
    pseudoInv = np.dot(np.linalg.inv(np.dot(np.transpose(xCoords), xCoords)), np.transpose(xCoords))

    weights = np.dot(pseudoInv, ysignTarg)

    w0 = weights[0]
    w1 = weights[1]
    w2 = weights[2]
    w3 = weights[3]
    w4 = weights[4]
    w5 = weights[5]

    # Monte Carlo simulation
    x2 = range(numPointsMonte)

    # y-coordinates of random data
    ydat2 = range(numPointsMonte)

    # y-coordinates of hypothesis
    yhypo2 = range(numPointsMonte)

    # signs for target
    ysig2 = range(numPointsMonte)

    nonoise = range(numPointsMonte)

    # signs for hypothesis
    ysigHypo2 = range(numPointsMonte)

    for i in range(numPointsMonte):
        # x-coordinates
        x2[i] = random.random()*2.0 - 1.0

        # y-coordinates of random data
        ydat2[i] = random.random()*2.0 - 1.0
	
        # figure out the sign
        if (x2[i]**2 + ydat2[i]**2 - 0.6 > 0):
            ysig2[i] = 1
            nonoise[i] = 1
        else:
            ysig2[i] = -1
            nonoise[i] = -1

        if(w0*1 + w1*x2[i] + w2*ydat2[i] + w3*x2[i]*ydat2[i] + w4*x2[i]**2 + w5*ydat2[i]**2 > 0):
            yhypo2[i] = 1
        else:
            yhypo2[i] = -1

    for i in range(int(numPointsMonte*0.1)):
        ysig2[i] = ysig2[i]*-1

        if(ysig2[i] != yhypo2[i]):
            outofsample += 1

print "the number of misclassified out of sample points are: ", outofsample  

