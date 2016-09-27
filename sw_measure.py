#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

filename = "interfaces.txt"
file = open(filename,"r")
receive_sum = [];
transmit_sum = [];
i = j = -1
while 1:
    line = file.readline()
    if not line:
	    break
    if line.find("Kernel") == -1:
	    pass
    else:
        receive_sum.append(0)
        transmit_sum.append(0)
        i = i + 1
        j = 0
    if line.find("s201-") == -1:
        pass
    else:
        j += 1
        if j > 1:
    	    str0 = line[19:29]
    	    receive_sum[i] += int(str0)
            print "j is : %d" %j
            print int(str0)
        else: 
            str0 = line[45:59]
            transmit_sum[i] += int(str0)
            print "j is : %d" %j
            print int(str0)

print receive_sum
print transmit_sum
ReceivePkt = receive_sum[1] - receive_sum[0]
TransminPkt = transmit_sum[1] - receive_sum[0]
print ReceivePkt
print TransminPkt
#rate = (ReceivePkt - TransminPkt) / ReceivePkt
#print "The packet loss rate is : %f" % rate