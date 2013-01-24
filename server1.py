#! /usr/bin/python

import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

pktnum = 0

while True:
	if(pktnum%10000==0):
		print "Sending packet",pktnum
	socket.send("%d" % (pktnum))
	pktnum+=1

