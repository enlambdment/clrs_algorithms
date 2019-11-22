def linear_search(lst,v):
	n = len(lst)
	j = 0
	while j < n:
		if lst[j] == v:
			return(j)
		else:
			j = j+1
	return(None)

if __name__ == '__main__':
	l = input('Please provide a list of integers without brackets: ')
	l = l.split(',')
	l_ints = []
	for n in l:
		l_ints.append(int(n))
	v = input('Please provide an integer to search for: ')
	v = int(v)
	srch = linear_search(l_ints,v)
	if srch == None:
		print('Your input was missing from the list!')
	else:
		print('Your input is in the list, at index position: ', srch)