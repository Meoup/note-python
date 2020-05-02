def check(bullets):
    # 检查子弹，如为奇数，则+1
    for i in range(len(bullets)):
        if bullets[i] % 2 != 0:
            bullets[i] += 1


def distribute(bullets):
    # 调整分配 此在检查之后进行，即所有子弹均为偶数
    b = [0] * len(bullets)
    # 先减半
    for i in range(len(bullets)):
        bullets[i] = bullets[i] // 2  # 子弹减半
        if i + 1 == len(bullets):
            b[0] = bullets[i]
        else:
            b[i + 1] = bullets[i]  # 作为下一个士兵的增量
    # 然后给下一个士兵加子弹
    for i in range(len(bullets)):
        bullets[i] += b[i]


def count(bullets):
    # 计算结果
    i = 0
    while min(bullets) != max(bullets):
        # 先检查
        check(bullets)
        # 然后分发
        distribute(bullets)
        # 记一次
        i += 1
        print(f"第{i}次调整后：{bullets}")


if __name__ == '__main__':
    bullets = [12, 2, 8, 22, 16, 4, 10, 6, 14, 20]
    count(bullets)


