#!/usr/bin/python
#
# SMTP VRFY Script by tarxien
# 
# Support for VRFY assumed, you should confirm this first
#
# This script takes two arguments - server IP and input file
# File should be plain text with a username on each line
#

import socket
import sys

#check for arguments
if len (sys.argv) != 3:
	print "Usage: smtp_vrfy.py <server ip> <inputfile>"
	sys.exit(1)

#read server IP
ServerIP = sys.argv[1]

#open username input file
infile = open(sys.argv[2])
 
#go through file line by line, sending VRFY + username to server
for line in infile:

	# Create a Socket
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect to the Server
	connect=s.connect((ServerIP,25))
	# Receive the banner and print to screen
	banner=s.recv(1024)
	print banner
	# VRFY a user and print result
	s.send('VRFY ' + line + '\r')
	result=s.recv(1024)
	print result
	# Close the socket
	s.close()
