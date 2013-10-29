#!/usr/bin/python

from scipy import optimize
import numpy as np
from math import*
import sys
import os
from random import*

def constantf(x, b):
    return b

def linearf(x, a):
    return a*x

def linearbf(x, a, b):
    return a*x + b

def quadf(x, a):
    return a*x**2

def quadbf(x, a, b):
    return a*x**2 + b

numberofreps = 1000
numberofpts = 1000
numberofmonte = 1000

totalb = 0
constant = 0

linconst = 0
slope = 0

lin = 0
linbf = 0
quad = 0
quadobf = 0

for a in range(numberofreps):
    points = [0]*numberofpts

    # choose random points in the range of -1 to 1
    for i in range(numberofpts):
        points[i] = random()*2 - 1

    # choose two points from the random points list
    point1x = points[randint(0, numberofpts - 1)]

    point2x = points[randint(0, numberofpts - 1)]

    point1y = sin(pi*point1x)

    point2y = sin(pi*point2x)

    xcoords = np.array([point1x, point2x])
    ycoords = np.array([point1y, point2y])

    x0 = np.array([0.0])
    xline = np.array([0.0])
    xlinebf = np.array([0.0, 0.0])
    xquad = np.array([0.0])
    xquadbf = np.array([0.0, 0.0])

    paramsconst, params_covariance_const = optimize.curve_fit(constantf, xcoords, ycoords, x0)

    paramslinear, params_covariance_linear = optimize.curve_fit(linearf, xcoords, ycoords, xline)

    paramslinbf, params_covariance_linbf = optimize.curve_fit(linearbf, xcoords, ycoords, xlinebf)

    paramsquad, params_covariance_quad = optimize.curve_fit(quadf, xcoords, ycoords, xquad)

    paramsquadbf, params_covariance_quadbf = optimize.curve_fit(quadbf, xcoords, ycoords, xquadbf)

    linconst += paramslinear[0]

    slope += paramslinear[0]

    points = [0]*numberofmonte

    constantTotal = 0
    linTotal = 0
    linbfTotal = 0
    quadTotal = 0
    quadbfTotal = 0

    for b in range(numberofmonte):
        # choose random points in the range of -1 to 1
        points[b] = random()*2 - 1

    for c in range(numberofmonte):
        constantTotal += (paramsconst[0] - sin(pi*points[c]))**2

    for d in range(numberofmonte):
        linTotal += (paramslinear[0]*points[d] - sin(pi*points[d]))**2

    for e in range(numberofmonte):
        linbfTotal += (paramslinbf[0]*points[e] + paramslinbf[1] - sin(pi*points[e]))**2

    for f in range(numberofmonte):
        quadTotal += (paramsquad[0]*points[f]**2 - sin(pi*points[f]))**2

    for g in range(numberofmonte):
        quadbfTotal += (paramsquadbf[0] * points[g]**2 + paramsquadbf[1] - sin(pi*points[g]))**2

    constant += constantTotal/numberofmonte

    lin += linTotal/numberofmonte

    linbf += linbfTotal/numberofmonte

    quad += quadTotal/numberofmonte

    quadobf += quadbfTotal/numberofmonte

print "the average mean square error for constant is: ", constant/numberofreps

print "the average slope of the linear function is: ", linconst/numberofreps

print "the average mean square error for the linear function y = ax is: ", lin/numberofreps

print "the average mean square error for the linear function y = ax + b is: ", linbf/numberofreps

print "the average slope of y = ax + b is: ", slope/numberofreps

print "the average mean square error for the quadratic function y = ax^2 is: ", quad/numberofreps

print "the average mean square error for the quadratic function y = ax^2 + b is: ", quadobf/numberofreps
