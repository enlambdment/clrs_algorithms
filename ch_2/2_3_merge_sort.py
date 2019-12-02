import random

def merge(ar, p, q, r):
	# set up new subarray
	n = r - p + 1
	srtd = [None] * n # 0, .., n-1
	d = 0
	i = p
	j = q+1
	while i <= q and j <= r:
		if ar[i] < ar[j]:
			srtd[d] = ar[i]
			i = i+1
		else:
			srtd[d] = ar[j]
			j = j+1
		d = d+1
	# after while loop exits, need to handle 
	# cases where
	# 1. j > r - may be left-over elements i, .., q
	# Need to fill in srtd[d] .. srtd[n-1] with
	# ar[i] .. ar[q]
	# 2. similar if i > q - may be left-over elements j, .. r.
	if j > r:							
		l_count = q - i
		for x in list(range(0, l_count+1)):
			srtd[d+x] = ar[i+x]
	elif i > q:
		r_count = r - j
		for x in list(range(0, r_count+1)):
			srtd[d+x] = ar[j+x]
	# now update 'srtd' vals back into ar
	# srtd[0] -> ar[p], ..
	# .. srtd[n-1] -> ar[r] = ar[(n-1)+p]
	for y in list(range(0, n)):
		ar[p+y] = srtd[y]


# myArray = [1,3,7, 2,5,6]
# print(merge(myArray, 0, 2, 5))

# myArray = [1,3,7, 2,5,6,12,13,14]
# print(merge(myArray, 0, 2, 8))

# myArray = [1,2,3,6,7, 4,5]
# print(merge(myArray, 0, 4, 6))

# e.g. [ar[m], ..., ar[n]]
# length:	(n-m) + 1 = l
# split:	k = floor(l/2)
# [ar[m],     ..., ar[m+k]];
# [ar[m+(k+1)], ..., ar[n]]

def rec_merge_sort(ar, m, n):
	# is the array short enough to be already 'sorted'?
	l = (n - m) + 1 # this needs to *decrease* with every
					# rec' procedure call!
	if l == 1:
		# don't change anything
		ar[m:n] = ar[m:n]
	else:
		# split up into 2 subarrays; sort each in place,
		# then merge the results
		k = l // 2
		# merge-sort left subarray
		rec_merge_sort(ar, m,   m+k-1)
		# merge-sort right subarray
		rec_merge_sort(ar, m+k,   n)
		# merge the two sorted subarrays
		merge(ar, m, m+k-1, n)

def merge_sort(ar):
	length = len(ar)
	rec_merge_sort(ar, 0, length-1)
	return(ar)

# trying it out on random arrays

rand_len = random.randint(0,30)
rand_nums = []
for j in list(range(0,rand_len)):
	n = random.randint(0,100)
	rand_nums.append(n)

print("My random array:", rand_nums)

sortedAr = merge_sort(rand_nums)
print(sortedAr)			# at least after running 'merge_sort', 
						# the array has been sorted in place.

idx = 0
while idx < rand_len-1:
	is_srtd_at_idx = rand_nums[idx] <= rand_nums[idx+1]
	if not is_srtd_at_idx:
		print("Sort failure at index:", str(idx), "!")
		break
	else:
		idx = idx+1

if idx == rand_len-1:
	print("Sort success!")





