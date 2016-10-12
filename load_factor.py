#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import sys

"""This code is used to get the load factor of the network
   argv[1] means how many hosts are included(from h1 to hargv[1])
   argv[2] means the total bandwidth"""
n = int(sys.argv[1])
sum_num = 0
denominator = float(sys.argv[2])
speed_array = []
with open('h201.txt', 'r') as f:
    lines =  f.readlines()
    for i in xrange(-200,-200+n):
        line = lines[i]
        j = line.find("Mbit")
    	speed_array.append(float(line[j-6:j]))

for i in range(n):
	sum_num += speed_array[i]

sum_num = sum_num / 1000
print "The total speed of h1 to h%s is %f Gbit/s,the total bandwidth is %f Gbit/s" %(sys.argv[1],sum_num,denominator)
print "The load factor is %f" % (sum_num/denominator)