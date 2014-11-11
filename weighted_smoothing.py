#!/usr/bin/python
#
#
#
# Kim Brugger contact: kim@brugger.dk

import sys
import pprint
import re
import os
pp = pprint.PrettyPrinter(indent=4)


values = (4,5,9,14,20,25,30)


#
# Does local smoothing of values by doing a weighted average.
#
def smooth( v ):

	weights = (0.15, 0.70, 0.15)
	
	smooth_v = []
	smooth_v.append( v[ 0 ])

	for i in range(1, len(v) - 1):
		value = (weights[0] * v[ i - 1 ]) + (weights[1] * v[ i ]) + (weights[2] * v[i + 1])
		smooth_v.append( value )

	smooth_v.append( v[ -1 ])

	return smooth_v

values = smooth( values )

pp.pprint( values )


