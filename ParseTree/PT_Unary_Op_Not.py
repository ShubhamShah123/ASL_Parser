# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Unary_Op_Not() :
	def __init__( self, value ) :
		self.m_Value = value

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+1)) + "UNARYOP 'not'")
#---------#---------#---------#---------#---------#--------#
