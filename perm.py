import itertools


def poss_combination(string):
	
	length = len(string)
	
	n =0
	k = []
	for p in range(2,length+1):							#loop to get words of size from to n
		for i in itertools.permutations(string,p):		#returns all possible permutaion of given words of size p
			k.append(''.join(map(str,i)))

	return k


	