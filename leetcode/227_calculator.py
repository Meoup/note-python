def calculate(s):
    """
    类表达式字符串的计算器功能，实现"+、-、*、/"的功能
    :param s: str
    :return: int

    Example :
        Input: "3+2*2"
        Output: 7

    思路：
        把所有的计算都转换为加法运算
    """
    num, sigh = 0, "+"
    res = []
    for i in range(len(s)):
        if s[i].isdecimal():
            num = num*10 + ord(s[i]) - ord("0")
        if (not s[i].isdecimal() and not s[i].isspace()) or i == len(s)-1:
            if sigh == "+":
                res.append(num)
            elif sigh == "-":
                res.append(-num)
            elif sigh == "*":
                res.append(res.pop()*num)
            else:
                res.append(res.pop()//num)
            sigh = s[i]
            num = 0
    print(res)
    return sum(res)


if __name__ == '__main__':
    print(calculate("4 + 4 * 2 / 5 + 9 * 2 - 10"))
