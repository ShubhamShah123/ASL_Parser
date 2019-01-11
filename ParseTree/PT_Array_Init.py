# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Array_Init() :
	def __init__( self, expr1, expr2 ) :
		self.m_expr1 = expr1
		self.m_expr2 = expr2

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+2)) + "ARRAY CONSTRUCTOR")
		print( (INDENTSTR*(indent+2)) + "INIT ")
		self.m_expr1.dump(indent+3)
		print( (INDENTSTR*(indent+2)) + "OF")
		self.m_expr2.dump(indent+3)
#---------#---------#---------#---------#---------#--------#
