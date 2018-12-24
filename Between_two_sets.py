#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    la=[]
    for i in range(a[n-1],b[0]+1):
        if [len(list(i for x in range(m) if b[x]%i==0)),len(list(i for x in range(n) if i%a[x]==0))]==[m,n]:
            la.append(i)
    return len(la)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
