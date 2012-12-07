#! /usr/bin/python

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.connect("tcp://localhost:5557")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt(zmq.SUBSCRIBE, zip_filter) 	# Must SUBSCRIBE to get any messages (subscribe to "" to get all)

# Process 5 updates
total_temp = 0
for update_nbr in range(5):
	string = socket.recv()
	print "Received",string
	zipcode, temperature, relhumidity = string.split()
	total_temp += int(temperature)

print "Average temperature for zipcode '%s' was %dF" % (zip_filter, total_temp / update_nbr)


