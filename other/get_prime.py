from math import sqrt


def is_prime(n):
    """
    判断输入的数字 n 是否是质数
    :param n: int
    :return: boolean
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        print(i)
        if n % i == 0:
            return False
    return True


def print_prime(n):
    # 埃氏筛法：每次都把对应的素数的倍数筛走
    # 打印素数
    prime = []
    for i in range(n + 1):
        prime.append(True)
    for i in range(2, n + 1):
        # 先从2开始，把是2的倍数的数都剔除。
        if prime[i]:
            print(i)
            j = i + i
            while j <= n:
                prime[j] = False
                j += i


if __name__ == '__main__':
    print(is_prime(25))
