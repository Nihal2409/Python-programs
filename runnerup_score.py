if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    l=[]
    l.append(arr[0])
    for i in range(n):
        if(l[0]>arr[i]):
            l.append(arr[i])
            break
    print(l[1])

