from itertools import product
k,m = map(int,input().split())
lis =[]
for i in range(k):
    lis.append(sorted(list(map(int, input().split())))[1:])

l = list(set(product(*lis)))
fl = []
for i in l:
    f = [x**2 for x in i]
    fl.append(f)
z =[]
for i in fl:
    z.append(sum(i)%m)
print(max(z))
