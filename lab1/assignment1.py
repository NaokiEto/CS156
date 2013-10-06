import random

listIter = range(1000)
misclassified = 0

for num in range(1000):

    # coordinates for line
    a1 = random.random()*2.0 - 1.0
    a2 = random.random()*2.0 - 1.0 

    b1 = random.random()*2.0 - 1.0
    b2 = random.random()*2.0 - 1.0

    slope = (b2 - b1) / (a2 - a1)

    x = range(100)
    y = range(100)

    # y-coordinates of random data
    ydat = range(100)

    # signs
    ysig = range(100)

    for i in range(100):

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

    # initializing
    w0 = 0
    w1 = 0
    w2 = 0

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

        misList = []
        tList = []

        # figure out if each point is classified or misclassfied
        # if misclassified, correct w

        # get the misclassfied points
        while(i < 99):
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

    # Monte Carlo simulation
    x2 = range(1000)
    y2 = range(1000)

    # y-coordinates of random data
    ydat2 = range(1000)

    # y-coordinates of hypothesis
    yhypo2 = range(1000)

    # signs for target
    ysig2 = range(1000)

    # signs for hypothesis
    ysigHypo2 = range(1000)

    for i in range(1000):
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
            misclassified += 1

total = 0
for term in range(1000):
    total += listIter[term]

average = total/1000.0

print total
print average
print misclassified

