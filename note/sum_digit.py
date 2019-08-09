def get_sum(num):
    """求一个整数的所有位数之和"""
    sum_digit = 0
    for i in range(len(str(num))):
        remind = num % 10  # 取个位数
        sum_digit += remind
        num = int(num / 10)  # 把个位数去掉
    return sum_digit


if __name__ == '__main__':
    print(get_sum(323369889332))
