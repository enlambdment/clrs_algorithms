def insertion_sort(lst):
	length = len(lst)
	for j in list(range(1,length)):
		# retrieve the value to be compared
		# with each element in the just-preceding,
		# already-sorted subsequence
		key = lst[j]
		# get upper boundary of just-prec. subseq.
		i = j-1
		while i >= 0 and lst[i] > key:
			lst[i+1] = lst[i]
			i = i-1
		lst[i+1] = key
	return(lst)

def decr_insertion_sort(lst):
	length = len(lst)
	for j in list(range(1,length)):	# i.e. the numbers from 1, 2 ... (length-1)
		key = lst[j]
		i = j-1
		while i >= 0 and lst[i] < key:
			lst[i+1] = lst[i]
			i = i-1
		lst[i+1] = key
	return(lst)

if __name__ == '__main__':
	l = input('Please provide a list of integers without brackets: ')
	l = l.split(',')
	l_nums = []
	for n in l:
		l_nums.append(int(n))
	# srt = insertion_sort(l_nums)
	srt = decr_insertion_sort(l_nums)
	print('The sorted list: ', srt)
