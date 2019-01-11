# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Assign() :
	def __init__( self, lvalue, expression ) :
		self.m_Value = lvalue
		self.m_Expression = expression


	def dump( self, indent = 0 ) :
		print( (INDENTSTR*indent) + 'ASSIGN')
		self.m_Value.dump(indent+1)
		self.m_Expression.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
