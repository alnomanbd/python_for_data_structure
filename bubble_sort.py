#!/usr/bin/env python
__author__ = "Al Noman"

def Bubble_Sort(list_item):
	"""
	Implementation of Bubble Sort. O(n2) and thus highly ineffective
	"""
	size = len(list_item) - 1
	for i in range(size,0,-1):
		for j in range(i):
			if(list_item[j] > list_item[j+1]):
				temp = list_item[j]
				list_item[j] = list_item[j+1]
				list_item[j+1] = temp
	return list_item
	
def Test_Bubble_Sort(module_name = "this_module"):
	list_item = [7,2,5,1,6,10,4,9,3,8]
	assert(Bubble_Sort(list_item) == sorted(list_item))
	print(Bubble_Sort(list_item))
	
if __name__ == "__main__":
	Test_Bubble_Sort()
