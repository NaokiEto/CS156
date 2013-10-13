from random import*

firstavg = 0
randavg = 0
leastavg = 0

zeroten = 0

numberOf = 0

for a in range(10000):
    # number of flips for each of 100 coins
    tenFlips = range(500)

    # total flips
    tenthousand = range(5000)

    for i in range(5000):
	    tenthousand[i] = randint(0, 1)

    for j in range(500):
        tenFlips[j] = 0
        for k in range(10):
            tenFlips[j] += tenthousand[j*10+k]

    # random coin to choose
    randcoin = randint(0, 499)

    firstavg += tenFlips[0]

    randavg += tenFlips[randcoin]

    leastavg += min(tenFlips)

    if ((min(tenFlips) <= 1) or (min(tenFlips) >= 9)):
        numberOf += 1

print "the average number of heads for the first coin is: ", float(firstavg)/float(10000)

print "the average number of heads for random coin is: ", float(randavg)/float(10000)

print "the average number of minimum heads for coin is: ", float(leastavg)/float(10000)

print "the number of minimum heads that are 0, 1, 9, or 10 is: ", numberOf
    
    
