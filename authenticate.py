#!/usr/bin/python

#Authenticate

#http://www.pythoncentral.io/hashing-strings-with-python/

import hashlib

key=None
while not key:
	key=raw_input("Enter password")

hash=hashlib.md5(key).hexdigest()

f=open("hashFile","r")
# The read() object adds a \n to the end of the string value. 
# The rstrip('\n') removes it.
fileHash=f.read().rstrip('\n')
f.close()
if hash==fileHash:
	print "auth OK"
else:
	print "auth Failed"

print fileHash
print hash
