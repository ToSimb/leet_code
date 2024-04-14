# Recursion
def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    first = bool(s) and p[0] in [s[0], "."]
    if len(p) > 1 and p[1] == "*":
        return isMatch(s, p[2:]) or (first and isMatch(s[:1], p))
    else:
        return first and isMatch(s[1:], p[1:])

# Dynamic programming (Bottom - Up)
def isMatch2(s: str, p: str) -> bool:
    mas = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    mas[-1][-1] = True
    for i in range(len(s)+1):
        print (mas[i])
    print ("++++++")
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            first = i < len(s) and p[j] in {s[i], "."}
            if (j + 1 < len(p)) and (p[j+1] == "*"):
                mas[i][j] = mas[i][j+2] or (first and  mas[i+1][j])
            else:
                mas[i][j] = first and mas[i+1][j+1]
    
    for i in range(len(s)+1):
        print (mas[i])
    return mas[0][0]

# Dynamic programming (Bottom - Up)
def isMatch3(s: str, p: str) -> bool:
    hmap = {}
    def mas(i,j):
        if (i,j) not in hmap:
            if j == len(p):
                answer = i == len(s)
            else:
                first = i < len(s) and p[j] in [s[i], "."]
                if (j + 1 < len(p)) and (p[j+1] == "*"):
                    answer = mas(i,j+2) or (first and mas(i+1,j))
                else:
                    answer = first and mas(i + 1, j + 1)
            hmap[i, j] = answer
            print (hmap, " : " )
            print ("i - ", i, " : j - ", j, " :: ", answer)
        return hmap[i,j]
    return mas(0,0) 


if "__name__" == "__name__":
    s = "asdd"
    p = "as*d."
    print (isMatch3(s, p))

