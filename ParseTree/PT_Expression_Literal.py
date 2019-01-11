# Shah, Shubham B.
# 2018-12-6
#---------#---------#---------#---------#---------#--------#
from .common import *
import random

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Literal() :
	
	def __init__( self, kind, value ) :
		self.m_Value = value
		self.m_Kind = kind

	def dump( self, file_name = '', indent = 0 ) :

		if self.m_Kind == "STRING": 
			print( (INDENTSTR*(indent+2)) + "LITERAL " + self.m_Kind + " '"+ self.m_Value[1:len(self.m_Value)-1] +"'")
			with open(file_name, "a") as fp:
				fp.write((INDENTSTR*(indent+2)) + "LITERAL " + self.m_Kind + " '"+ self.m_Value[1:len(self.m_Value)-1] +"'\n")
		else:
			print( (INDENTSTR*(indent+2)) + "LITERAL " + self.m_Kind + " '"+ self.m_Value +"'")
			with open(file_name, "a") as fp:
				fp.write((INDENTSTR*(indent+2)) + "LITERAL " + self.m_Kind + " '"+ self.m_Value +"'\n") 

	def semantic_check( self, file_name = '', indent = 0):
		flag = False
		if self.m_Kind == "REAL": 
			self.m_Value = float(self.m_Value)
			flag = True
		elif self.m_Kind == "INTEGER":
			int_value = int(self.m_Value)
			# ((2^(32-1))-1)
			if int_value <= ((2^31)-1): 
				flag = True
		else:
			for char in self.m_Value:
				if ord(char) < 128:
					flag = True
				else:
					flag = False
		if flag:
			return True
		else:
			return False


	def code_gen(self, file_name = '', indent = 0):
		val = random.sample(range(0,9), 1)[0]
		fp = open(file_name, 'a') 
		if self.m_Kind == "REAL":
			data_type = "REALIT0" + str(val)
			fp.write("\n.data\n.align\t8\n{0}:\t.double\t{1}\n.text\n\n".format(data_type, self.m_Value))
			fp.write("movq\t{0}, %xmm0\ncall writeReal\ncall writeNewLine\n\n".format(data_type))			

		elif self.m_Kind == "INTEGER":
			data_type = "INTLIT0" + str(val)
			fp.write("\n.data\n.align\t4\n{0}:\t.int\t{1}\n.text\n\n".format(data_type, self.m_Value))
			fp.write("movl\t{0}, %edi\ncall writeInteger\ncall writeNewLine\n\n".format(data_type))

		else:
			data_type = "STRLIT0" + str(val)
			fp.write("\n.data\n{0}:\t.asciz\t{1}\n.text\n\n".format(data_type, self.m_Value))
			fp.write("movq\t${0}, %rdi\ncall writeString\ncall writeNewLine\n\n".format(data_type))

#---------#---------#---------#---------#---------#--------#
