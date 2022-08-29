"""
working with finding common values in list
using hash and boolean
"""


def search(dat1 = None, dat2 = None):
	"""
	checkin for matches true or false
	:params dat1: list() of integers
	:params dat2: list() of integers
	return bool()
	"""
	assert dat1 is not None, "we must have some data"
	assert dat2 is not None, "must have data"
	my_dict = {}
	for i in dat1:
		my_dict[i] = True
	print(my_dict)
	for j in dat2:
		print(j)
		if j in my_dict:
			return True
	return False
	
	
if __name__ == "__main__":
	list1 = [1, 2, 3]
	list2 = [4, 5, 6]
	list2a = [4, 3, 6] # test case match
	print(search(list1, list2))
