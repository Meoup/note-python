def decode_string(s: str) -> str:
    """
    字符串的解码，例子如下：
        s = "3[a]2[bc]", return "aaabcbc".
        s = "3[a2[c]]", return "accaccacc".
        s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
    解法思路：
        首先要把数字和[]区分出来，然后采用栈的处理方式，先进后出，这样可以把里层的字符先处理，由内到外
    """
    # 最外层 1*字符串
    stack = [["", 1]]
    num = ""
    for ch in s:
        if ch.isdigit():
            # 如果是数字则记录下来
            num += ch
        elif ch == "[":
            # 开头
            stack.append(["", int(num)])
            num = ""
        elif ch == "]":
            # 结尾, 此刻需弹出
            c, n = stack.pop()
            stack[-1][0] += c*n
        else:
            # 中间的字符
            stack[-1][0] += ch
    print(stack[0][0])
    return stack[0][0]


if __name__ == '__main__':
    decode_string("2[abc]3[cd]ef")
