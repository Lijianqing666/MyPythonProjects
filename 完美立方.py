n = int(input(">>"))  # n范围内的立方数

list_cube = [0]  # 用于存储立方数的列表
for i in range(1, n + 1):
    list_cube.append(i * i * i)

for a in range(6, n + 1):
    for b in range(2, a - 1):
        if list_cube[a] < (list_cube[b] + list_cube[b + 1] + list_cube[b + 2]):
            break
        for c in range(b + 1, a):
            if list_cube[a] < (list_cube[b] + list_cube[c] + list_cube[c + 1]):
                break
            for d in range(c + 1, a):
                if list_cube[a] == (list_cube[b] + list_cube[c] + list_cube[d]):
                    print("Cube=%d,Tripe=(%d,%d,%d)" % (a, b, c, d))
