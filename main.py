if __name__ == '__main__':
    # 1
    s = input()
    s1 = s[:len(s) // 2 + len(s) % 2]
    s2 = s[len(s) // 2 + len(s) % 2:]
    result = s2 + s1
    print(result)

    # 2
    s = input()
    word1, word2 = s.split()
    result = word2 + " " + word1
    print(result)

    # 3
    s = input()
    first = s.find('f')
    last = s.rfind('f')
    if first == -1:
        pass
    elif first == last:
        print(first)
    else:
        print(first, last)

    # 4
    s = input()
    first = s.find('f')
    second = s.find('f', first + 1)
    if first == -1:
        print(-2)
    elif second == -1:
        print(-1)
    else:
        print(second)

    # 5
    s = input()
    first = s.find('h')
    last = s.rfind('h')
    result = s[:first] + s[last + 1:]
    result = result.replace('h', '', 2)
    print(result)

    # 6
    s = input()
    first = s.find('h')
    last = s.rfind('h')
    result = s[first + 1:last][::-1]
    result = s[:first + 1] + result + s[last:]
    print(result)

    # 7
    s = input()
    result = s.replace('1', 'one')
    print(result)

    # 8
    s = input()
    result = s.replace('@', '')
    print(result)

    # 9
    s = input()
    first = s.find('h')
    last = s.rfind('h')
    result = s[:first + 1] + s[first + 1:last].replace('h', 'H') + s[last:]
    print(result)

    # 10
    s = input()
    result = ''.join([s[i] for i in range(len(s)) if i % 3 != 0])
    print(result)