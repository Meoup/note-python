from collections import defaultdict, Counter


def group_anagrames(strs):
    """
    按同字母划分数组
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    :param strs: Str
    :return: List
    """
    ans = dict()
    for s in strs:
        key = get_ord(s)
        if not ans.get(key):
            ans[key] = []
        ans[key].append(s)
    print(ans.values())


def get_ord(s):
    code = [0] * 26
    for c in s:
        code[ord(c) - ord('a')] += 1
    return tuple(code)


if __name__ == '__main__':
    def countElements(arr: list) -> int:
        from collections import Counter

        counter = Counter(arr)
        ans = 0
        for item in counter:
            if (item + 1) in counter:
                ans += min(counter[item], counter[item + 1])
        print(ans)

    countElements([1,1,3,3,5,5,7,7])
