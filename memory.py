#! /usr/bin/python

instr_memory_40 = {
	  100 : 'movia R2_40 AVEC', 
	  104 : 'movia R3_40 BVEC', 
	  108 : 'movia R4_40 N_40', 
	  112 : 'ldw R4_40 R4_40',
	  116 : 'add R5_40 R0_40 R0_40',
	  120 : 'ldw R6_40 R2_40',
	  124 : 'ldw R7_40 R3_40',
	  128 : 'mul R8_40 R6_40 R7_40',
	  132 : 'add R5_40 R5_40 R8_40',
	  136 : 'addi R3_40 R3_40 4',
	  140 : 'addi R2_40 R2_40 4',
	  144 : 'subi R4_40 R4_40 1',
	  148 : 'bgt R4_40 R0_40 LOOP',
	  152 : 'stw R5_40 DOT_PRODUCT'
}

data_memory_40 = {
	2000 : 4,
	2004 : 3,
	2008 : 6,
	2012 : 2,
	3000 : 1,
	3004 : 3,
	3008 : 0,
	3012 : 2,
	4000 : 4,
	5000 : 0
}

name_mappings_40 = {
	'AVEC' : 2000,
	'BVEC' : 3000,
	'N_40' : 4000,
	'LOOP' : 120,
	'DOT_PRODUCT' : 5000
}
