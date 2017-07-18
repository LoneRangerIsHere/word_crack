import itertools


def poss_combination(string):
	
	length = len(string)
	print length
	n =0
	k = []
	for p in range(2,length+1):
		for i in itertools.permutations(string,p):
			k.append(''.join(map(str,i)))

	return k


	