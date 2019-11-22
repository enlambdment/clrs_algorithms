class Posn():
	"""Models a position during an addition of two positionally notated numbers."""

	def __init__(self, place=0, carry=0):
		"""Initialize place and carry attributes."""
		self.place = place
		self.carry = carry

# myPosn = Posn(0, 1)
# print(myPosn.place)
# print(myPosn.carry)

def sub_bin_add(c,a,b):
	s = c + a + b
	r_place = s % 2
	r_carry = s // 2
	r = Posn(r_place, r_carry)
	return(r)

# myR = sub_bin_add(1,1,1)
# print(myR.place)
# print(myR.carry)

def binary_addition(ar1, ar2):
	# assumption: len(ar1) == len(ar2)
	n = len(ar1)
	# initialize output array
	result = [0] * (n+1)
	j = 0
	carry = 0
	while j < n:
		r = sub_bin_add(carry, ar1[j], ar2[j])
		# populate result-array value, for current index
		result[j] = r.place
		carry = r.carry
		j = j+1
	result[n] = carry 
	return(result) 

myAr1 = [1,0,1,1,1]
myAr2 = [1,1,1,1,0]
mySum = binary_addition(myAr1, myAr2)
print(mySum)



