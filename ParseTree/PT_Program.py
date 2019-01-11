# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Program() :
	def __init__( self, block) :
		self.m_Block = block    

	def dump( self, file_name, indent = 0 ) :
		# print("#### FILE_NAME PROGRAM: ",file_name)
		print( (INDENTSTR*indent) + 'PROGRAM' )
		self.m_Block.dump( file_name, indent+1 )

	def semantic_check( self, file_name = '', indent = 0):
		self.m_Block.semantic_check(file_name)

	def code_gen(self, file_name = '', indent = 0):
		# print("### CODE_GEN: PT_Program ###")
		# print("-- FILE NAME CG : PT_Program : {0} --".format(file_name))
		
		with open(file_name, 'w') as fp:
			fp.write(".global main\n")
			fp.write(".text\n")
			fp.write("main:\n")
		fp.close()
		self.m_Block.code_gen(file_name, (indent + 1))
		with open(file_name, 'a') as fp:
			fp.write("    movl\t$0, %eax\n")
			fp.write("    leave\n")
			fp.write("    ret\n")

#---------#---------#---------#---------#---------#--------#
