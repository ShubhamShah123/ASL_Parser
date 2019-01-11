# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Block() :
	def __init__( self, items) :
		self.m_Value = items

	def dump( self, file_name, indent = 0 ) :
		# print("### FILE NAME BLOCK : ", file_name)
		print( (INDENTSTR*indent) + '{' )
		with open(file_name, "a") as fp:
			fp.write('PROGRAM\n{\n')
		for d in self.m_Value:		
			d.dump(file_name, indent+1)				
		print( (INDENTSTR*indent) + '}' )
		with open(file_name, "a") as fp:
			fp.write('}\n')

	def semantic_check( self, file_name = '', indent = 0):
		for d in self.m_Value:
			d.semantic_check(file_name, indent)


	def code_gen(self, file_name = '', indent = 0):
		# print("### CODE_GEN: PT_Block ###")
		# print("-- FILE NAME CG : PT_Block : {0} --".format(file_name))
		with open(file_name, 'a') as fp:
			fp.write((INDENTSTR*indent) + "pushq   %rbp\n")
			fp.write((INDENTSTR*indent) + "movq   %rsp, %rbp\n")
		fp.close()
		for d in self.m_Value:
			d.code_gen(file_name, (indent+1))

#---------#---------#---------#---------#---------#--------#
