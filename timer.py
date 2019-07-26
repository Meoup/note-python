import time
from functools import wraps


def timer(func):
	"""
	一个装饰器实现的计时器
	"""
	@wraps(func)
	def inner_func(*args, **kwargs):
		start = time.time()
		res = func(*args, **kwargs)
		print("%s 函数运行耗时：%s ms" % (func.__name__, (time.time() - start)*1000))
		return res

	return inner_func
