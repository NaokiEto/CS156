#!/usr/bin/python

from math import*
import sys
import os
from random import*

numberofreps = 10000
numberofpts = 1000

totalslope = 0

for a in range(numberofreps):
    points = [0]*numberofpts

    # choose random points in the range of -1 to 1
    for i in range(numberofpts):
        points[i] = random()*2 - 1

    bottom = 0
    while (bottom == 0):
        # choose two points from the random points list
        point1 = points[randint(0, numberofpts - 1)]

        point2 = points[randint(0, numberofpts - 1)]

        top = point1*sin(pi*float(point1)) + point2*sin(pi*float(point2))

        bottom = point1*point1 + point2*point2

    slope = float(top)/float(bottom)

    totalslope += slope

print "the average slope is: ", totalslope/numberofreps
