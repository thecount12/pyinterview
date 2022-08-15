"""
1,2,4
1,3,4
result 1,1,2,3,4,4
"""

def merge_sort(dat1=None, dat2=None):
	"""
	:params dat2: list() of integers
	:params dat2: list() of integers
	:return: dict()
	"""
	assert dat1 is not None, "Must have some data like a list"
	assert dat2 is not None, "Must be a list"
	assert type(dat1) and type(dat2) is list, "must have data inside list"
	assert type(dat1[1]) is int, "must be integers"
	new_list = []
	new_list = dat1
	for i in dat2:
		new_list.append(i)
	return sorted(new_list)
	
	
	
if __name__ == "__main__":
	list1 = [1, 2, 4]
	list2 = [1, 3, 4]
	# test case 1
	print(merge_sort(list1, list2))
	# unit test 1
	try:	
		print(merge_sort())
	except Exception as err1:
		print(err1)
	# unit test 2
	try:	
		print(merge_sort([], []))
	except Exception as err2:
		print(err2)
	# unit test 3
	try:	
		print(merge_sort([1, "two", 3], [1, 2, 3]))
	except Exception as err3:
		print(err3)
