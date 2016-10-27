#! /usr/bin/python
import sys
from stages import *
from registers import *
from memory import *

def main():
	i = 0
	j = 0
	while (i < 5):
		instruction = Stages_40.instr_fetch_40()
		Stages_40.decode_instr_40(instruction)
		Stages_40.execute_40(instruction)
		Stages_40.memory_access_40(instruction)
		Stages_40.write_back_40(instruction)

		for (a, b) in Registers_40.nios_registers_40.iteritems():
			print (a,b)
		i = i + 1
	while (j < 32):
		instruction = Stages_40.instr_fetch_40()
		Stages_40.decode_instr_40(instruction)
		Stages_40.execute_40(instruction)
		Stages_40.memory_access_40(instruction)
		Stages_40.write_back_40(instruction)

		for (a, b) in Registers_40.nios_registers_40.iteritems():
			print (a,b)
		j = j + 1
	
	instruction = Stages_40.instr_fetch_40()
	Stages_40.decode_instr_40(instruction)
	Stages_40.execute_40(instruction)
	Stages_40.memory_access_40(instruction)
	Stages_40.write_back_40(instruction)

	for (a, b) in Registers_40.nios_registers_40.iteritems():
		print (a,b)
	
	
	 
if __name__ == "__main__":
    	main()
