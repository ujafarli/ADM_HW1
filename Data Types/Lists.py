if __name__ == '__main__':
    N = int(input())
    res = []

# Depending on the commend print, remove, add or modify list
    for n in range(N):
        inp = input().split(" ")
        command = inp[0]
        if command == 'append':
            res.append(int(inp[1]))
        if command == 'insert':
            res.insert(int(inp[1]), int(inp[2]))
        if command == 'reverse':
            res = res[::-1]
        if command == 'print':
            print(res)
        if command == 'sort':
            res = sorted(res)
        if command == 'pop':
            res.pop()
        if command == 'remove':
            res.remove(int(inp[1]))

