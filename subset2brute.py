"""
subset brute force
"""

def subset_tool(data):
	formula = 2 ** len(data)
	print(f"formula: {formula }")
	size = len(data)
	ar = []
	num = 0	
	print(f"size: {size}")
	for i in range(formula):
		print(i)
		if i > size:
			print("oops")
			num += 1
		if data[num:i] not in ar:
			ar.append(data[num:i])
		if i == formula/2 + 1:
			ar.append([len(data)-1])
			data.pop(len(data)-2)
		if i == formula-1:
			if data not in ar:
				if data not in ar:
					ar.append(data)
	if formula == 4:
		ar.pop(size+1)
	print(ar)
	
if __name__ == "__main__":
	my_list = [1,2,3,4]
	subset_tool(my_list)

