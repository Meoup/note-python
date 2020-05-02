def permutation(S):
    ans = []
    state = ''
    s = set()

    def backtrack(state, S):
        if state in s:
            return
        s.add(state)
        if len(S) == 0:
            ans.append(state)
            return
        for i in range(len(S)):
            backtrack(state + S[i], S[:i] + S[i+1:])
    backtrack(state, S)
    print(ans)
    return ans


def permutation_1(S):
    ans = []
    S = sorted(S)

    def backtrack(pre_str, r_str):
        if not len(r_str):
            ans.append(pre_str)
        else:
            pre = ''
            for i in range(len(r_str)):
                if r_str[i] != pre:
                    backtrack(pre_str + r_str[i], r_str[:i] + r_str[i + 1:])
                pre = r_str[i]

    backtrack('', S)
    print(ans)
    return ans


if __name__ == '__main__':
    s = ['A', 'B', 'A', 'D']
    print(len(permutation(s)))
    print(len(permutation_1(s)))




