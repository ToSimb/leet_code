def polindrom1(x:int):
    if x < 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]

def polindrom2(x:int) -> bool:
    if (x < 0 ) or (x !=0 and x % 10 == 0):
        return False
    
    reversed_num = 0
    while x > reversed_num:
        reversed_num = (reversed_num * 10) + (x % 10)
        x = x //10
        print ("x:", x, " rev:", reversed_num)
    return (x == reversed_num) or (x == (reversed_num // 10))

if __name__ == __name__ :
    x = 10
    print (polindrom2(x))