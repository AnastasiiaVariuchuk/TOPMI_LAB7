if __name__ == '__main__':
    # 1
    # s = input()
    # s1 = s[:len(s) // 2 + len(s) % 2]
    # s2 = s[len(s) // 2 + len(s) % 2:]
    # result = s2 + s1
    # print(result)

    # 2
    # s = input()
    # word1, word2 = s.split()
    # result = word2 + " " + word1
    # print(result)

    # 3
    # s = input()
    # first = s.find('f')
    # last = s.rfind('f')
    # if first == -1:
    #     pass
    # elif first == last:
    #     print(first)
    # else:
    #     print(first, last)

    # 4
    # s = input()
    # first = s.find('f')
    # second = s.find('f', first + 1)
    # if first == -1:
    #     print(-2)
    # elif second == -1:
    #     print(-1)
    # else:
    #     print(second)

    # 5
    s = input()
    first = s.find('h')
    last = s.rfind('h')
    result = s[:first] + s[last + 1:]
    result = result.replace('h', '', 2)
    print(result)
