class BinarySearchTree:
    """
    实现二叉搜索树结构的类型
    简称 BST
    """
    def __init__(self, node):
        # 节点
        self.node = node
        # 左节点
        self.left = None
        # 右节点
        self.right = None

    def insert(self, val):
        """插入"""
        if self.node > val:
            # 小于当前节点的插入到左节点
            if self.left is None:
                # 如果左节点不存在，则新增节点
                self.left = BinarySearchTree(val)
            else:
                # 如果存在，则插入到该节点
                self.left.insert(val)
        else:
            # 大于当前节点的插入到右节点
            if self.right is None:
                self.right = BinarySearchTree(val)
            else:
                self.right.insert(val)


def order(tree, res):
    """
    对二叉搜索树进行排序
    :param tree: BinarySearchTree
    :param res: []
    :return: None
    """
    if tree:
        # 先取左边节点
        order(tree.left, res)
        res.append(tree.node)
        # 再去右边的
        order(tree.right, res)


def sort_list(nums):
    """
    二叉树排序算法
    :param nums: list
    :return: list
    """
    length = len(nums)
    if length < 2:
        return nums
    # 先构建BST
    tree = BinarySearchTree(nums[0])
    for i in range(1, length):
        tree.insert(nums[i])
    # 获取排序结果
    res = []
    order(tree, res)
    return res


if __name__ == '__main__':
    print(sort_list([9, 7, 5, 3, 3, 1, 4, 6, 8]))
