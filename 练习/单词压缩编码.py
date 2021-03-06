def minimumLengthEncoding(words):
    """
    给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
    例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
    对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
    那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
    示例：
        输入: words = ["time", "me", "bell"]
        输出: 10
        说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
    把重复的单词或在已有单词里成员单词去掉
    :param words:
    :return:
    """
    s = set(words)
    for word in words:
        for i in range(1, len(word)):
            s.discard(word[i:])
    return sum(len(w) + 1 for w in s)


if __name__ == '__main__':
    print(minimumLengthEncoding(["time", "me", "bell", 'football', 'foot', 'ball']))
