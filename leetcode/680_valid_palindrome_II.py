def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    c = "abccba"
    print(is_palindrome(c))
