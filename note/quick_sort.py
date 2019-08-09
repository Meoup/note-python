def quick_sort(nums):
	"""
	快速排序算法：
	在列表中随机取一个元素，把大于和小于该元素的其他元素分成两个列表，然后按从小到大的顺序排列好
	在新生成的两个列表中重复上述操作
	递归 直到 列表长度小于2
	时间复杂度： O(n*log n)  空间复杂度： O(log n)
	最糟情况： O(n^2)
	稳定性：不稳定
	"""
	if len(nums) < 2:
		return nums
	# 取一个元素
	pivot = nums[0]
	less_nums = [item for item in nums[1:] if item <= pivot]
	greater_nums = [item for item in nums[1:] if item > pivot]
	return quick_sort(less_nums) + [pivot] + quick_sort(greater_nums)


if __name__ == '__main__':
	print(quick_sort([20, 4, 3, 1, 2, 8, 9, 10, 5, 6]))
