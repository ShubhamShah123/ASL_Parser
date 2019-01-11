# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_LValue() :
	def __init__( self, value) :
		self.m_Value = value

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+1)) + "EXPRESSION")
		self.m_Value.dump(indent = indent+1)
#---------#---------#---------#---------#---------#--------#
