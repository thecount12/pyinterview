
def solution(nums, ans, cur, index):
	if index > len(nums):
		return
	ans.append(cur[:])
	for i in range(index, len(nums)):
		if nums[i] not in cur:
			cur.append(nums[i])
			solution(nums, ans, cur, i)
			cur.pop()
	return
		
def subsets(nums):
	ans = []
	cur = []
	solution(nums, ans, cur, 0)
	return ans


bar = subsets([1,2,3, 4])
print(bar)
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

