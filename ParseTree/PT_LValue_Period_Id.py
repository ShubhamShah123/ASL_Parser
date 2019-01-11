# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_LValue_Period_Id() :
	def __init__( self, value, component ) :
		self.m_Value = value
		self.m_Component = component

	def dump( self, indent = 0 ) :
		print( (INDENTSTR*(indent+2)) + "LVALUE RECORD COMPONENT")
		self.m_Value.dump(indent+1)
		print( (INDENTSTR*(indent+3)) + "COMPONENT '" + self.m_Component+ "'")
		# self.m_Compnent.dump(indent+2)
#---------#---------#---------#---------#---------#--------#
