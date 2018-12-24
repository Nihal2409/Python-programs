n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    name, *num = input().split()
    if name=='remove':
        s.remove(int(*num))
    elif name=='discard':
        s.discard(int(*num))
    else:
        s.pop()
sum=0
for i in s:
    sum+=i
print(sum)