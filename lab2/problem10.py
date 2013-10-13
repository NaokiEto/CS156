import random
import numpy as np

misclassified = 0

outofsample = 0

numPoints = 1000

w0total = 0
w1total = 0
w2total = 0
w3total = 0
w4total = 0
w5total = 0

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
    
    w0total += w0
    w1total += w1
    w2total += w2
    w3total += w3
    w4total += w4
    w5total += w5  

    # Monte Carlo simulation
    x2 = range(numPoints)

    # y-coordinates of random data
    ydat2 = range(numPoints)

    # y-coordinates of hypothesis
    yhypo2 = range(numPoints)

    # signs for target
    ysig2 = range(numPoints)

    nonoise = range(numPoints)

    # signs for hypothesis
    ysigHypo2 = range(numPoints)

    for i in range(numPoints):
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

    for i in range(int(numPoints*0.1)):
        ysig2[i] = ysig2[i]*-1

        if(nonoise[i] != yhypo2[i]):
            outofsample += 1

print "the number of misclassified out of sample points are: ", outofsample  

w0avg = w0total/1000
w1avg = w1total/1000
w2avg = w2total/1000
w3avg = w3total/1000
w4avg = w4total/1000
w5avg = w5total/1000

print "the weights are: ", w0avg, w1avg, w2avg, w3avg, w4avg, w5avg
