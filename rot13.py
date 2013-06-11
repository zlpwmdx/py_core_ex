#!/usr/bin/env python
# rot13 -- exer 7-10
import string

upperletters = string.ascii_lowercase
lowerletters = string.ascii_uppercase

rot13map = {}

def rot13map_init():
	if len(rot13map) != 0:
		return
	
	for s in (upperletters, lowerletters):
		l = len(s)/2
		for i in xrange(l):
			rot13map[s[i]] = s[l+i]
			rot13map[s[l+i]] = s[i]
	#print rot13map


def rot13(string):
	rot13map_init()

	convert_s = ''
	for c in string:
		convert_s += rot13map.get(c, c)
	return convert_s

def showmenu():
	while True:
		try:
			s = raw_input('Enter string to rot13:')
		except:
			print '\nQuit!'
			break;

		print 'Your string to en/decrypt was: [%s].' %s
		print 'The rot13 string is: [%s].' %(rot13(s))
		print

if __name__ == '__main__':
	showmenu()
