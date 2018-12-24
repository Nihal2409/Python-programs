def minion_game(s):
    kevinsc=0
    stuartsc=0
    length=len(s)
    for i in range(length):
        if s[i] in 'AEIOU':
            kevinsc+=(length-i)
        else:
            stuartsc+=(length-i)
    if kevinsc>stuartsc:
        print('Kevin',kevinsc)
    elif stuartsc>kevinsc:
        print('Stuart',stuartsc)
    else:
        print('Draw')
if __name__ == '__main__':