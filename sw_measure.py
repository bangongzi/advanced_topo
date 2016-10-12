#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

def pkt_count(fname,sname,tx_num):
    file = open(fname,"r")
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
        if line.find(sname) == -1:
            pass
        else:
            j += 1
            if j > tx_num:
    	        str0 = line[19:29]
    	        receive_sum[i] += int(str0)
            else: 
                str0 = line[45:59]
                transmit_sum[i] += int(str0)
    ReceivePkt = receive_sum[i] - receive_sum[i-1]
    TransmitPkt = transmit_sum[i] - transmit_sum[i-1]
    print "Now switch %s has received %d packets" %(sname,ReceivePkt)
    print "Now switch %s has transmitted %d packets" %(sname,TransmitPkt)
    rate = (ReceivePkt - TransmitPkt) / ReceivePkt
    print "The packet loss rate of %s is : %f" %(sname,rate)

fname = 'interfaces.txt'
if len(sys.argv) == 2:
    if sys.argv[1] == '301':
        pkt_count(fname,'s301',1)
    elif sys.argv[1] == '201':
        pkt_count(fname,'s201',1)
    elif sys.argv[1] == '101':
        pkt_count(fname,'s101',4)
    else:
        print "Please input 201 ,301 or 101"
else:
    "The right input form is like:sw_measure.py 301"