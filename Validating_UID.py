# Enter your code here. Read input from STDIN. Print output to STDOUT
def isUniqueChars2(string):
    myset=set(string)
    return len(myset)
def uppercase1(string):
    COUNT = 0
    for c in string:
        if(c.isupper()):
            COUNT=COUNT+1
    return COUNT
def number(string):
    COUNT = 0
    for c in string:
        if (c.isdigit()):
            COUNT=COUNT+1
    return COUNT
n=int(input())
l=[]
for i in range(0,n):
    temp=raw_input()
    l.append(temp)
first=l[0]
for i in range(0,n):
    if(len(l[i])==10 and l[i].isalnum() and isUniqueChars2(l[i])==10 and uppercase1(l[i])>=2 and number(l[i])>=3):
        print("Valid")
    else:
        print("Invalid")
    
            