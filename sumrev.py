"""
2,4,3
5,6,4
res = 7,0,8
its really 
342 + 465 = 807
"""

def rev_something(dat=None):
	"""
	:params dat: list() of integers
	:return int
	"""
	assert dat is not None, "Must have something in args"
	assert len(dat) > 1, "must have integers in here"
	rev = dat[::-1]
	result = int("".join(map(str, rev)))
	return result
	
	
def sum_tool(dat1=None, dat2=None):
	"""
	:params dat1: list() of integers
	:params dat2: list() of integers
	:return: list() of sum of both integers in reverse
	"""
	
	assert dat1 and dat2 is not None, "Must have something in here"
	assert len(dat1) > 1, "list should not be empty"
	my_list = []
	try:
		total = rev_something(dat1) + rev_something(dat2)
		for item in str(total):
			my_list.insert(0, int(item))
	except:
		pass
	return my_list

	
if __name__ == "__main__":
	list1 = [2, 4, 3]
	list2 = [5, 6, 4]
	print(sum_tool(list1, list2))
	# unit test 1
	try:
		print(sum_tool())
	except Exception as err1:
		print(err1)
	# unit test 2
	try:
		print(sum_tool([], list2))
	except Exception as err2:
		print(err2)
		
	
