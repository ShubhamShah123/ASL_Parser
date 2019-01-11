# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Write() :
	def __init__( self, expression ) :
		self.m_Expression = expression


	def dump( self, file_name, indent = 0 ) :
		# print("### FILE NAME STATEMENT WRITE: ", file_name)
		for i in self.m_Expression:
			with open(file_name, "a") as fp:
				fp.write((INDENTSTR*indent) + 'WRITE\n')
				fp.write((INDENTSTR*(indent+1)) + 'ARG\n')
			print( (INDENTSTR*indent) + 'WRITE')
			print( (INDENTSTR*(indent+1)) + 'ARG')
			i.dump(file_name, indent)
	
	def semantic_check( self, file_name = '', indent = 0):
		for i in self.m_Expression:
			return_value = i.semantic_check(file_name, indent)
			if return_value:
				# print("continue")
				continue
			else:
				# print("break")
				break


	def code_gen(self, file_name = '', indent = 0):
		# print("### CODE_GEN: PT_Statement_Write ###")
		for i in self.m_Expression:
			i.code_gen(file_name, (indent+1))
			# print("--- RETURNED FROM I CODE_GEN ---")


#---------#---------#---------#---------#---------#--------#
