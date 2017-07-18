#num =0
lst = []
import time
import perm
import os
from sort import LengthSort
saved_path = os.getcwd()
os.chdir(r"D:\python_programs\projects\word_crack\dictionary")

def magic(string):
	p = perm.poss_combination(string)		#returns all possible permutaion of give aplha
	
	for y in p :
		compare(y)							#check if it is a meaningful word
	

def remove_duplicate(l):
	return list(set(l))

def compare(combination):

	root= os.listdir(r"D:\python_programs\projects\word_crack\dictionary")
	
	for file_name in root:				#checks for all files in the folder dictionary

	
		with open(file_name) as f:
			for line in f:
					if combination == line.strip():				#strip is used because line has a new line at the end ,so we need to remove it
							lst.append(line.strip())							
					


ch = 'yes'


while ch != 'exit' :

		os.system('cls')		#clear the screen
		
		string = raw_input("\nEnter words--")
		print "\nCracking....\n"

		lst = []				#clear the list of previous result
		
		beg = time.time()
		magic(string)			#function that cracks words and stores in global var lst[]	
		end = time.time()

		if len(lst) == 0:
			print "No meaningful words can be formed"


		print_list = remove_duplicate(lst)		
		
		srt = LengthSort()
		
		print_list = srt.sort(print_list)		#sort the list in the order of their size

		print print_list
		
		print "\nWords cracked :", len(print_list)
		print "Time taken :", end-beg, "seconds"

		ch = raw_input("\nType exit to close the program, enter to continue\n")
		ch = ch.lower()

os.chdir(saved_path)
#compare()
#print num		