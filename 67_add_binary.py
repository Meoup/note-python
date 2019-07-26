def add_binary(a, b):
    """
    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"

    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

    :param a:str
    :param b:str
    :return:str

    解题思路：
    这是考验算法的能力，所以内置函数 int()必然是不可使用的。
    两个类二进制字符串的相加，规则是按照二进制运算相加
    转化为根据末位的字符来处理，可以分为3类 1+1，1+0，0+0
    每处理一次就剔除该末位继续处理
    使用递归处理:
    基线条件就是当其中一个字符串已经全部运算
    """
    if len(a) == 0:
        # 代表a的长度小于b，则返回剩余的b
        return b
    if len(b) == 0:
        # 代表b的长度小于a，则返回剩余的a
        return a
    if a[-1] == '1' and b[-1] == '1':
        # 当a,b的末位都是'1'的时候，需要进位 0
        return add_binary(add_binary(a[:-1], b[:-1]), '1') + '0'
    elif a[-1] == '0' and b[-1] == '0':
        # 不需要进位
        return add_binary(a[:-1], b[:-1]) + '0'
    else:
        return add_binary(a[:-1], b[:-1]) + '1'


if __name__ == '__main__':
    print(add_binary('11101', '1001011'))
