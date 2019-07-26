from collections import deque  # deque 是双端队列


def bfs(name):
    """
    广度优先搜索算法的使用:
        查找你的人际关系网中是否有名叫'meoup'的人（包括朋友的朋友）
    :param name: str
    :return: boolean
    """
    # 创建队列
    search_queue = deque()
    # 把自己的朋友压入队列
    search_queue += graph[name]
    # 记录已搜索过的人
    searched = []
    # 直到队列为空，搜索结束
    while search_queue:
        # 把最左边的人弹出
        person = search_queue.popleft()
        # 判断是否已经搜索过
        if person not in searched:
            if person == "meoup":
                # 找到返回 True
                return True
            else:
                # 没找到则把这个朋友的朋友放入队列
                search_queue += graph[person]
                # 并把他放入已搜索的列表中
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {
        "you": ["hello", "world", "lily", "david"],
        "hello": ["coop", "vn", "lily"],
        "world": ["play"],
        "lily": ["charge", "hello"],
        "david": [],
        "coop": [],
        "vn": [],
        "play": ["meoup"],
        "charge": [],
        "meoup": []
    }
    print(bfs("you"))
