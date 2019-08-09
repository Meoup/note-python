def can_place_flowers(flowerbed, n):
    """
    种花问题
    :param flowerbed: List[int]
    :param n: int
    :return: Boolean
    """
    num = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            num += 1
    return num >= n


if __name__ == '__main__':
    print(can_place_flowers([0, 0, 0, 0, 1, 0, 1, 0], 3))
