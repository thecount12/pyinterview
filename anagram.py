"""
anagram stuff
array = ["eat", "tea", "tan", "nat", "ant"]
"""
from collections import defaultdict

def my_hash(key, val):
	if "".join(sorted(key)) == "".join(sorted(val)):
		return True
	else:
		return False

def ana(data=None):
	m_dict = defaultdict(str)
	clean_list = []
	"""
	for i in range(len(data)):
		print(i) # int of index
		print(data[i]) # string
		for j in data:
			print(f"j: {j}") # j strings
			if j == data[i]:
				print("cool")
				#if "".join(sorted(j)) == "".join(sorted(data[i])):
				#	
				#	print(True)
				print("".join(sorted(j)))
					
			else:
				print("darn")
	"""
	
	
	for i in data:
		if "".join(sorted(i)) not in "".join(sorted(list(m_dict.keys()))):
			print("cool")
			m_dict[i] = i
		else:
			print("missing or different")
			
	print(m_dict)

	
	"""
	foo = {"bar": "foo", "tea": "tea"}
	print(type(foo))
	print(type(list(foo.keys())))		
	"""
	
if __name__ == "__main__":
	m_array = ["eat", "tea", "tan", "nat", "ant"]
	ana(m_array)
