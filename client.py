#! /usr/bin/python

import time
import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect("tcp://localhost:5556")
# socket.connect("tcp://localhost:5557")
socket.connect("tcp://95.138.176.230:5556")	# Rackspace
socket.connect("tcp://95.138.176.230:5557")

filter = sys.argv[1] if len(sys.argv) > 1 else ""
socket.setsockopt(zmq.SUBSCRIBE, filter) 	# Must SUBSCRIBE to get any messages (subscribe to "" to get all)

last_msg = 0
start = time.time()
pktnum = 0
while True:
	msg = int(socket.recv())
	if(msg != last_msg+1):
		print "Sequence error:",last_msg,msg
	last_msg = msg

	if(msg % 100000 == 0):
		elapsed = time.time()-start
		print "Received",pktnum,"packets in",elapsed,"s = ",pktnum/elapsed,"pkts/sec"

	pktnum = pktnum+1

print "DONE: *****************"


