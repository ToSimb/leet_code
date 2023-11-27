import math
# functions
def reverse1 ( x: int) -> int:
    maxInt = 2 ** 31 - 1
    minInt = -2 ** 31
    y = 0
    val = True if x > 0 else False
    x = abs(x)
    while (x!= 0):
        y = y * 10 + (x % 10)
        x = x // 10
        if (x > maxInt or x < minInt) :
            return 0
    if val:
        return y
    else:
        return -y

def reverse2 ( x: int) -> int:
    maxInt = 2 ** 31 - 1
    minInt = -2 ** 31
    y = 0

    while x != 0:
        if y > maxInt /10 or y < minInt / 10:
            return 0
        digit = x % 10 if x > 0 else x % -10
        y = y * 10 + digit
        x = math.trunc(x / 10)
    return y

if __name__ == __name__ :
    x = -131241230
    print (reverse2(x))