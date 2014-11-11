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



def merge_int_arrays( a1, a2):


	a1 = sorted( a1, key = int )
	a2 = sorted( a2, key = int )

	pp.pprint( a1 )
	pp.pprint( a2 )


	merged_array = []

	while ( len (a1) or len( a2 )  ):

		if ( len (a1) and len( a2 )):
			if ( a1[ 0 ] < a2 [ 0 ]):
				merged_array.append( a1.pop(0))
			else:
				merged_array.append( a2.pop(0))
		elif( len( a1 )):
			merged_array.append( a1.pop(0))
		else:
			merged_array.append( a2.pop(0))




	return merged_array

pp.pprint( merge_int_arrays( [1,3,4,5], [2,9,5,10,6]))

