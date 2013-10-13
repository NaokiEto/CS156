from random import*

firstavg = 0
randavg = 0
leastavg = 0

zeroten = 0

for a in range(100000):
    # number of flips for each of 100 coins
    tenFlips = range(1000)

    # total flips
    tenthousand = range(10000)

    for i in range(10000):
	    tenthousand[i] = randint(0, 1)

    for j in range(1000):
        tenFlips[j] = 0
        for k in range(10):
            tenFlips[j] += tenthousand[j*10+k]

    # random coin to choose
    randcoin = randint(0, 999)

    firstavg += tenFlips[0]

    randavg += tenFlips[randcoin]

    leastavg += min(tenFlips)

    for b in range(1000):
        if(tenFlips[b] == 0):
            zeroten += 1
        elif (tenFlips[b] == 10):
            zeroten += 1

print "the average number of heads for the first coin is: ", float(firstavg)/float(100000)

print "the average number of heads for random coin is: ", float(randavg)/float(100000)

print "the average number of minimum heads for coin is: ", float(leastavg)/float(100000)

print "the number of zero heads or ten heads for 10 flips is: ", zeroten
    
    
