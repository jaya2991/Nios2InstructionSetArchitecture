#! /usr/bin/python
from memory import *
from registers import *
from instruction import *

class Stages_40:
	NUM_STAGES_40 = 5
	ALUOutput_40 = 0
	LMD_40 = 0

	@staticmethod
	def instr_fetch_40():
		fetched_instr_40 = Instruction_40(instr_memory_40[Registers_40.PC_40])
		Registers_40.PC_40 = Registers_40.PC_40 + 4
		return fetched_instr_40

	@staticmethod
	def decode_instr_40(fetched_instr_40):
		fetched_instr_40.parse_instr_40()
		
	@staticmethod
	def execute_40(fetched_instr_40):
		if(fetched_instr_40._op == 'movia'):
			Stages_40.ALUOutput_40 = fetched_instr_40._Imm_40
			
		if(fetched_instr_40._op == 'ldw'):
			Stages_40.ALUOutput_40 = Registers_40.nios_registers_40[fetched_instr_40._A_40]	
		
		if(fetched_instr_40._op == 'add'):
			Stages_40.ALUOutput_40 = Registers_40.nios_registers_40[fetched_instr_40._A_40] + Registers_40.nios_registers_40[fetched_instr_40._B_40]
		
		if(fetched_instr_40._op == 'mul'):
			Stages_40.ALUOutput_40 = Registers_40.nios_registers_40[fetched_instr_40._A_40] * Registers_40.nios_registers_40[fetched_instr_40._B_40]
		
		if(fetched_instr_40._op == 'addi'):
			Stages_40.ALUOutput_40 = Registers_40.nios_registers_40[fetched_instr_40._A_40] + int(fetched_instr_40._Imm_40)

		if(fetched_instr_40._op == 'subi'):
			Stages_40.ALUOutput_40 = Registers_40.nios_registers_40[fetched_instr_40._A_40] - int(fetched_instr_40._Imm_40)

		if(fetched_instr_40._op == 'bgt'):
			if(Registers_40.nios_registers_40[fetched_instr_40._B_40] > Registers_40.nios_registers_40[fetched_instr_40._A_40]):
				Stages_40.ALUOutput_40 = fetched_instr_40._Imm_40
			else:
				Stages_40.ALUOutput_40 = Registers_40.PC_40

		if(fetched_instr_40._op == 'stw'):
			Stages_40.ALUOutput_40 = fetched_instr_40._Imm_40
			
		
		
	@staticmethod
	def memory_access_40(fetched_instr_40):
		if(fetched_instr_40._op == 'ldw'):
			Stages_40.LMD_40 = data_memory_40[Stages_40.ALUOutput_40]
		elif(fetched_instr_40._op == 'bgt'):
			Registers_40.PC_40 = Stages_40.ALUOutput_40
		elif(fetched_instr_40._op == 'stw'):
			data_memory_40[Stages_40.ALUOutput_40] = Registers_40.nios_registers_40[fetched_instr_40._B_40]
		else:
			pass
		

	@staticmethod
	def write_back_40(fetched_instr_40):
		if(fetched_instr_40._op == 'ldw'):
			Registers_40.nios_registers_40[fetched_instr_40._B_40] = Stages_40.LMD_40

		else:
			if(fetched_instr_40._type == 'I-type'):
				if(fetched_instr_40._op == 'bgt'):
					pass
				else:
					Registers_40.nios_registers_40[fetched_instr_40._B_40] = Stages_40.ALUOutput_40
			elif(fetched_instr_40._type == 'R-type'):
				Registers_40.nios_registers_40[fetched_instr_40._Rd_40] = Stages_40.ALUOutput_40		
					
		
