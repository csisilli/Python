#!/usr/bin/env python3
import sys
maxTemp={}
for line in sys.stdin:
	line=line.strip()
	month,val= line.split(',')
	try:
		val=int(val)
	except ValueError:
		continue

	try:
		if  maxTemp[month]<= val:
			maxTemp[month]=val
		else:
			continue
	except:
		maxTemp[month]=val

for key in maxTemp.keys():
	print('%s\t%s' % (month,maxTemp[month]))
