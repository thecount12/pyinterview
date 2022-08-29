"""
first = [5,8,9,3,5,7,1,3,4,9,3,5,1,8,4]
second = [3,5,7,2]
output = [3,3,3,5,5,5,7,1,1,4,4,8,8,9]
"""

def sort_tool(dat=None, fixed=None):
	f_arr = []
	reg_ar = []
	for i in range(len(fixed)): # small array
		for j in range(len(dat)):  # large array
			if fixed[i] == dat[j]:
				# print(f"fixed: {i} {fixed[i]} :: dat {j} val {dat[j]}")
				f_arr.append(dat[j])
	for x in dat:
		if x not in f_arr:
			reg_ar.append(x)
	foo = f_arr + sorted(reg_ar)
	print(foo) # or return 


if __name__ == "__main__":
	first = [5,8,9,3,5,7,1,3,4,9,3,5,1,8,4]
	second = [3,5,7,2]
	print("test1")
	sort_tool(first, second)
