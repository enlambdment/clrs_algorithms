import random

def bin_insert(ar, v):
	# print the inputs that have been given
	# print("Insert:", v)
	# print("into the list:", ar)
	# starting out - don't know where to insert
	# GOAL: locate array indices i, j=i+1
	# s.t. inserting v after ar[i] & before ar[j]
	# results in 'ar' being sorted
	l_ar = len(ar)
	idx_L = 0
	idx_R = l_ar
	m = (idx_R - idx_L) // 2
	while idx_R - idx_L > 1:
		# distinguish 2 subarrays: we'll determine
		# which to insert into
		# print("Left subarray:",  ar[idx_L:   idx_L+m])
		# print("Right subarray:", ar[idx_L+m: idx_R])
		# select midpoint
		midpoint = ar[idx_L+m-1]
		# print("Is", v, "less than", midpoint, "?")
		if v < midpoint:
			# print("Prepare to insert into left subarray.")
			idx_R = idx_L + m 
		else:
			# print("Prepare to insert into right subarray.")
			idx_L = idx_L + m 
		# print("New bounds for possible index are:",
			# idx_L, ",", idx_R)
		# re-calculate m based upon new search bounds
		m = (idx_R - idx_L) // 2
	# the loop exits once idx_R - idx_L == 1.
	# to conclude, compare ar[idx_L] vs. v:
	# if v > ar[idx_L], then v should go to idx_L + 1;
	# otherwise, keep it there
	posn = idx_L
	# print("Compare", v, "versus", ar[posn])
	if v > ar[idx_L]:
		posn = posn + 1
	# print("Search concluded: v should replace position:", posn)
	# finally, conduct the insertion into sorted-position
	ar = ar[0:posn] + [v] + ar[posn:]
	# print("The new list with v in sorted position is:", ar)
	return(ar)

'''
# give a random length up to a max' length
# *non-empty list* needed as argument to 'bin_insert'
rand_len = random.randint(1,10)

# generate random list having that length
rand_lst = []
for j in list(range(0, rand_len)):
	n = random.randint(0, 100)
	rand_lst.append(n)

# by stipulation, the list passed to 'bin_insert'
# is always meant to be already sorted:
rand_lst = sorted(rand_lst)

# generate a random value to insert
rand_v = random.randint(0, 100)

bin_insert(rand_lst, rand_v)
'''


def bin_insert_sort(ns):
	j = 1
	length = len(ns)
	while j < length:
		print("j =", j)
		srtd_to_j = bin_insert(ns[0:j], ns[j])
		print("Sorted list up to", j, "is:", srtd_to_j)
		print("Replacing:", ns[0:j+1])
		ns[0:j+1] = srtd_to_j
		j = j+1
	return(ns)


rand_len = random.randint(0,15)

rand_lst = []
for j in list(range(0,rand_len)):
	n = random.randint(0,100)
	rand_lst.append(n)

print("Here's a random list:", rand_lst)
print("The sorted list:", bin_insert_sort(rand_lst))





