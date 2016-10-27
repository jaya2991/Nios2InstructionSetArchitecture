#! /usr/bin/python

from memory import *

class Instruction_40:
	instruction_type_40 = {
		'movia' : 'I-type',
		'ldw' 	: 'I-type',
		'mul'   : 'R-type',
		'add'	: 'R-type',
		'addi'	: 'I-type',
		'subi'  : 'I-type',
		'bgt'   : 'I-type',
		'stw'   : 'I-type'
	}

	def __init__(self, string_40):
		self._string_40 = string_40
		self._type_40 = None
		self._A_40 = None
		self._B_40 = None
		self._Imm_40 = None
		self._op = None
		self._Rd_40  = None

	def parse_instr_40(self):
		instr_list_40 = self._string_40.split(' ')
		self._type = Instruction_40.instruction_type_40[instr_list_40[0]]
		self._op = instr_list_40[0]
		if(self._type == 'I-type' and len(instr_list_40) == 3):
			self._B_40 = instr_list_40[1]
			if(self._op == 'movia' or self._op == 'stw'):
				self._Imm_40 = name_mappings_40[instr_list_40[2]]
			elif(self._op == 'ldw'):
				self._A_40 = instr_list_40[2]
		elif(self._type == 'I-type' and len(instr_list_40) == 4):
			self._B_40 = instr_list_40[1]
			self._A_40 = instr_list_40[2]
			if(self._op == 'bgt'):
				self._Imm_40 = name_mappings_40[instr_list_40[3]]
			else:
				self._Imm_40 = instr_list_40[3]
		else:
			self._Rd_40 = instr_list_40[1]
			self._B_40 = instr_list_40[2]
			self._A_40 = instr_list_40[3]

		
