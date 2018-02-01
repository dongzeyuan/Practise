# coding=UTF-8
# 输入3个数，按升序输出

def low_to_high(a, b, c):
    if a >= b and a >= c:
        high = a
        if b >= c:
            mid = b
            low = c
        else:
            mid = c
            low = b
           
    elif b >= a and b >= c:
        high = b
        if a >= c:
            mid = a
            low = c
        else:
            mid = c
            low = a
    elif c >= a and c >= b:
        high = c
        if a >= b:
            mid = a
            low = b
        else:
            mid = b
            low = a
    print(low, mid, high)
if __name__ == '__main__':
    a = int(input('Please enter the 1st num: '))
    b = int(input('Please enter the 2nd num: '))
    c = int(input('Please enter the 3rd num: '))
    low_to_high(a, b, c)
