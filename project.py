n = int(input())
s = [1]
for i in range(n):
    print(str(' '.join([str(j) for j in s])).center(100))
    s = [1] + [s[j]+s[j+1] for j in range(i)] + [1]