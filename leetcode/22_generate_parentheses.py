def generate_parenthese(n):
    """
    回溯法
    :param n:
    :return:
    """
    ans = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    print(ans)


if __name__ == '__main__':
    generate_parenthese(4)

