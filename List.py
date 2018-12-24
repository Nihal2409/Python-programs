n = int(input())
l=[]
for _ in range(n):
    name, *num= input().split()
    if name=='insert':
        l.insert(int(num[0]),int(num[1]))
    elif name=='remove':
        l.remove(int(num[0]))
    elif name=='append':
        l.append(int(num[0]))
    elif name=='sort':
        l.sort()
    elif name=='reverse':
        l.reverse()
    elif name=='print':
        print(l)
    elif name=='pop':
        l.pop()
    else:
        break

