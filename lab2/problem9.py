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

Atotal = 0
Btotal = 0
Ctotal = 0
Dtotal = 0
Etotal = 0

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

    x2 = [0]*numPoints

    # y-coordinates of random data
    ydat2 = [0]*numPoints

    # signs
    mysig = [0]*numPoints

    choiceA = [0]*numPoints
    choiceB = [0]*numPoints
    choiceC = [0]*numPoints
    choiceD = [0]*numPoints
    choiceE = [0]*numPoints

    Amatch = 0
    Bmatch = 0
    Cmatch = 0
    Dmatch = 0
    Ematch = 0

    for i in range(1000):

        # x-coordinates
        x2[i] = random.random()*2.0 - 1.0

        # y-coordinates of random data
        ydat2[i] = random.random()*2.0 - 1.0

        # figure out the sign for my hypothesis
        if ( w0 + w1*x2[i] + w2*ydat2[i] + w3*x2[i]*ydat2[i] + w4*x2[i]**2 + w5*ydat2[i]**2 > 0):
            mysig[i] = 1
        else:
            mysig[i] = -1

        # figure out the sign for choice A
        if (-1 - 0.05*x2[i] + 0.08*ydat2[i] + 0.13*x2[i]*ydat2[i] + 1.5*x2[i]**2 + 1.5*ydat2[i]**2 > 0):
            choiceA[i] = 1
        else:
            choiceA[i] = -1

        # figure out the sign for choice B
        if (-1 - 0.05*x2[i] + 0.08*ydat2[i] + 0.13*x2[i]*ydat2[i] + 1.5*x2[i]**2 + 15*ydat2[i]**2 > 0):
            choiceB[i] = 1
        else:
            choiceB[i] = -1

        # figure out the sign for choice C
        if (-1 - 0.05*x2[i] + 0.08*ydat2[i] + 0.13*x2[i]*ydat2[i] + 15*x2[i]**2 + 1.5*ydat2[i]**2 > 0):
            choiceC[i] = 1
        else:
            choiceC[i] = -1

        # figure out the sign for choice D
        if (-1 - 1.5*x2[i] + 0.08*ydat2[i] + 0.13*x2[i]*ydat2[i] + 0.05*x2[i]**2 + 0.05*ydat2[i]**2 > 0):
            choiceD[i] = 1
        else:
            choiceD[i] = -1

        # figure out the sign for choice E
        if (-1 - 0.05*x2[i] + 0.08*ydat2[i] + 1.5*x2[i]*ydat2[i] + 0.15*x2[i]**2 + 0.15*ydat2[i]**2 > 0):
            choiceE[i] = 1
        else:
            choiceE[i] = -1

        if(mysig[i] == choiceA[i]):
            Amatch += 1
        if(mysig[i] == choiceB[i]):
            Bmatch += 1
        if(mysig[i] == choiceC[i]):
            Cmatch += 1
        if(mysig[i] == choiceD[i]):
            Dmatch += 1    
        if(mysig[i] == choiceE[i]):
            Ematch += 1

    Atotal += Amatch
    Btotal += Bmatch
    Ctotal += Cmatch
    Dtotal += Dmatch
    Etotal += Ematch

print "the weights are: ", w0, w1, w2, w3, w4, w5
print "the totals for A, B, C, D, and E are: ", Atotal, Btotal, Ctotal, Dtotal, Etotal
