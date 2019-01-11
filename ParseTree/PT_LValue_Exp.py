# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_LValue_Exp() :
	def __init__( self, lvalue, expression ) :
		self.m_LValue = lvalue
		self.m_Expression = expression

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+2)) + "LVALUE ARRAY SUBSCRIPT")
		self.m_LValue.dump(indent+2)
		self.m_Expression.dump(indent+2)
#---------#---------#---------#---------#---------#--------#
