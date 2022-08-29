"""
script to find target but mostly we want 
sum zero but could be applied to other things
"""

def compute(dat=None, target=None):
	"""
	searching for sum adding to 10
	:params dat: list of integers
	:return: None
	"""
	assert dat is not None, "must have data here"
	assert target is not None, "must have an integer"
	found = []
	single = []
	for i in range(len(dat)):
		#print(i)
		for j in range(i, len(dat)):
			# print(f"i{dat[i]}, j{dat[j]}")
			if dat[i]+dat[j] == target:
				# print(f"sub {i},{j}")  # the answer here but for returns I need to test
				if i==j:
					#print(f"{[dat[i]]}")
					single.append(i)
				else:
					#print(f"[{dat[i]},{dat[j]}]")
					found.append([i,j])
	if len(single) > 0:
		found.append(single)
		return found
	else:
		return found
			
	


if __name__ == "__main__":
	my_list = [1, 3, 5, 7, 2]
	print("test1")
	print(compute(my_list, target=10))
	print("test2")
	print(compute([1, 3, 6, 7, 2], target=10))
	print("test3")
	print(compute([1, 3, 6, 7, -6], target=0))
