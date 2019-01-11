# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_UnaryOp() :
	def __init__( self, op, value ) :
		self.m_Value = value
		self.m_Op = op

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+1)) + "EXPRESSION")
		self.m_Op.dump(indent+1)
		self.m_Value.dump(indent+1)
#---------#---------#---------#---------#---------#--------#
