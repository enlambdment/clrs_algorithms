def selection_sort(lst):
	n = len(lst)
	for j in list(range(0,n-1)): 	# 0, 1, ..., n-2: 
		key = lst[j]				# *only* the first n-1 
		min_idx = j					# items of the list
		i = j+1
		for k in list(range(i,n)):
			if lst[k] < key:
				key = lst[k]
				min_idx = k
		# exchg. elements
		lst[min_idx] = lst[j]
		lst[j] = key
	return(lst)

# lst1 = [2]				# [2]
# lst2 = [2,3,4]			# [2,3,4]
# lst3 = [3,1,5,7]		# [1,3,5,7]
# lst4 = [3,1,4,2,7,5]	# [1,2,3,4,5,7]

# print(selection_sort(lst1))
# print(selection_sort(lst2))
# print(selection_sort(lst3))
# print(selection_sort(lst4))