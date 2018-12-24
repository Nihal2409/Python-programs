from collections import defaultdict
d=defaultdict(list)
choice=[]
n,m=list(map(int,input().split()))
for i in range(1,n+1):
    k=input()
    d[k].append(i)
for _ in range(m):
    choice.append(input())
for i in range(m):
    if choice[i] in d.keys():
        print(" ".join(map(str, d[choice[i]])))
    else:
        print(-1)