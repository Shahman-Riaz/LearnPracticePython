for i in range(int(input())):
    (a, b, c) = map(int, input().split(' '))
    print('YES') if (a <= c and c < b) else print('NO')