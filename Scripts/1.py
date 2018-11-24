N = int(input("N是什么"))

a = []
for i in range(N):
    if i <= 1:
        a.append(1)
    else:
        a.append(a[i-1] + a[i-2])

print(a)