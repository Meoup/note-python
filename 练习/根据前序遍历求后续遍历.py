class Tree:
    def __init__(self, x):
        self.node = x
        self.left = None
        self.right = None


def change_order(nums):
    if nums:
        root = Tree(nums.pop(0))
        p = [[], []]
        [p[val > root.node].append(val) for val in nums]
        root.left = change_order(p[0])
        root.right = change_order(p[1])
        return root


def post_order(ans, root):
    if root:
        post_order(ans, root.left)
        post_order(ans, root.right)
        ans.append(root.node)


if __name__ == '__main__':
    # 根据二叉搜索树的前序遍历 构建起后续遍历数组
    a = [6, 4, 1, 5, 9, 7, 10]
    res = []
    tree = change_order(a)
    post_order(res, tree)
    print(res)

