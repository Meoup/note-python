from other.stack import Stack


def decimal_convert(num, base):
    """
    十进制数转换成其他进制
    :param num: int
    :param base: int
    :return: str
    """
    digits = "0123456789ABCDEF"
    remind = Stack()

    while num > 0:
        rem = num % base
        remind.push(rem)
        num = num // base

    res = ""
    while not remind.is_empty():
        res += digits[remind.pop()]
    print(res)
    return res


if __name__ == '__main__':
    decimal_convert(10, 16)
