# parameters
s = "ABCDES"
numRows = 3 

# functions

def convert (s : str, numRows : int) -> str:
    if numRows <= 1 :
        return s
    
    mas = [[] for _ in range(numRows)]
    lvl = 0
    val = True

    for i in range(len(s)):
        mas[lvl].append(s[i])
        if val :
            lvl += 1
        else :
            lvl -= 1
        if lvl > numRows - 1 :
            lvl -= 2
            val = False
        if lvl < 0 :
            lvl += 2
            val = True
    sum = []
    for i in range(numRows):
        sum.extend(mas[i])
    return  ''.join(sum)

print (convert(s,numRows))