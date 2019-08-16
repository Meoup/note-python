def numJewelsInStones(J, S):
	"""
	统计J字符串中的字母在S中出现的次数之和
	:type J: str
	:type S: str
	:rtype: int
	"""
	# time.sleep(1)
	if len(J) == 0 or len(S) == 0:
		return 0
	count = 0
	for i in J:
		count += S.count(i)
	return count


if __name__ == '__main__':
	print(numJewelsInStones('zab', 'aAAbbbb'))
