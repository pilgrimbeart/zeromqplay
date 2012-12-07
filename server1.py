#! /usr/bin/python

import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

pktnum = 0

while True:
	zipcode = random.randrange(1,100000)

	# print "Sending packet",pktnum, zipcode,temperature,relhumidity
	socket.send("%d %d %d" % (zipcode, 1, 1))
	pktnum+=1

