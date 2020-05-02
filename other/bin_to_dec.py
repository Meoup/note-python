def bin_to_dec(bin_string):
    """
    把二进制字符串转换为整数
    :param bin_string: String
    :return: Integer
    例："01111" => 15
    int("01111", 2)
    """
    length = len(bin_string)
    num = 0
    for i in range(length):
        num += int(bin_string[i]) * 2**(length-i-1)
    return num


if __name__ == '__main__':
    print(bin_to_dec("0111111111"))
