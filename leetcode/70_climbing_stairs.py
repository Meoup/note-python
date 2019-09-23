def climb_stairs(n):
    """
    爬梯子问题:
        给定梯子的阶梯数n，一次只能爬1或者2个阶梯，请求出所有的不同的爬梯子的方法数目
    :param n: int
    :return: int
    思路：
        用 f(n) 表示爬 n 个梯子的方法
        则爬 n 个梯子的方法必然会有：f(n)=f(n-1)+f(n-2)，即当前数等于前两个数之和，斐波那契数列既视感
        也可使用递归，但是递归的话，会重复计算，时间复杂度

    """
    if n == 0:
        return 0
    else:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a


if __name__ == '__main__':
    print(climb_stairs(3))
