# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_LValue_ID() :
	def __init__( self, name ) :
		self.m_Value = name

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+1)) + "LITERAL")
		print( (INDENTSTR*(indent+2)) + "LVALUE ID '" + self.m_Value +"'" )
		
#---------#---------#---------#---------#---------#--------#
