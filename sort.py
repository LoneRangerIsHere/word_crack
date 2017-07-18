class LengthSort(object):

	def __init__(self):
		pass
	def sort(self,sort_list):

		#print sort_list
		n = len(sort_list)
		#print self.n
		for ind in range (0,n):
			
			
			for sec_ind in range(ind+1,n):
					curr_index = ind
					next_index = sec_ind
					
					curr_item = sort_list[curr_index]
					next_item = sort_list[next_index]
					#print curr_item
					#print next_item
					if(len(curr_item)>=len(next_item)):
						sort_list = self.switch_items(sort_list, curr_index, next_index)

		return sort_list

	def switch_items(self, sort_list, curr_ind, nex_ind):
			temp =	sort_list[curr_ind]
			sort_list[curr_ind] = sort_list[nex_ind]
			sort_list[nex_ind] = temp
			#print self.count 
			#print sort_list
			return sort_list
					



