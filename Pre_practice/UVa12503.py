t = int(input())
for tt in range(t):
    ans = 0
    c = []
    n = int(input())
    for i in range(n):
        s = input()
        if s[0] == 'R':
            ans += 1
            c.append(1)
        if s[0] == 'L':
            ans += -1
            c.append(-1)
        if s[0] == 'S':
            tmp = int(s.split()[2])
            ans += c[tmp - 1]
            c.append(c[tmp - 1])
    print(ans)