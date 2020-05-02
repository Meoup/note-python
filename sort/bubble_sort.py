from other.timer import timer


@timer
def bubble_sort(nums):
	"""
	冒泡排序算法：
		从第一个元素开始，比较相邻的两个元素，把更大的元素右移，直到排序完成
		需要比较的次数为 (n-1)*n
	时间复杂度： O(n^2)
	空间复杂度： O(1)
	稳定性：稳定
	"""
	if len(nums) < 2:
		return nums
	for i in range(len(nums)-1):
		is_sorted = False
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				is_sorted = True
				nums[j], nums[j+1] = nums[j+1], nums[j]
		if not is_sorted:
			break
	return nums


@timer
def bubble_sort_1(nums):
	"""
	冒泡排序算法：
		从第一个元素开始，比较相邻的两个元素，把更大的元素右移，直到排序完成
		需要比较的次数为 (n-1)*n
	时间复杂度： O(n^2)
	空间复杂度： O(1)
	稳定性：稳定
	"""
	if len(nums) < 2:
		return nums
	for i in range(len(nums)-1):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
	return nums


if __name__ == '__main__':
	print(bubble_sort([27, 1, 3, 7, 5, 2, 1, 3, 89, 73, 32, 27, 13, 6, 19]))
	print(bubble_sort_1([27, 1, 3, 7, 5, 2, 1, 3, 89, 73, 32, 27, 13, 6, 19]))

