#!/usr/bin/env python
# exercise 9-20

import gzip
import sys
import os

compsuffix = '.gz'

def usage():
	print 'Usage:', sys.argv[0], '[-c] filenamei[.gz]'
	sys.exit()

if len(sys.argv) != 2 and len(sys.argv) != 3:
	usage()

#compress
if len(sys.argv) == 2:
	filename = sys.argv[1]
	
	try:
		f_in = open(filename, 'rb')
		f_out = gzip.open(filename + compsuffix, 'wb')
	except:
		print 'File open error'
		sys.exit()

	f_out.writelines(f_in)
	f_out.close()
	f_in.close()		
#decompress
else:
	filename = sys.argv[2]
	fileext = os.path.splitext(filename)

	if sys.argv[1].lower() != '-c' or fileext[1] != compsuffix:
		usage()
	
	try:
		f_in = gzip.open(filename, 'rb')
		f_out = open(fileext[0], 'wb')
	except:
		print 'File open error'
		sys.exit()

	f_out.writelines(f_in)
	f_out.close()
	f_in.close()
