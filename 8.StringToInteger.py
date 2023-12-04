def mya( s: str) -> int:
    k = len(s)
    if k == 0:
        return 0
    lvl = 0
    val = 1
    y = 0
    i = 0 

    while i < k:
        cur_char = s[i]
        match lvl:
            case 2:
                if cur_char.isdigit():
                    lvl = 2
                    y = y*10 + int(cur_char)
                else:
                    break
            case 1:
                if cur_char.isdigit():
                    lvl = 2
                    y = y*10 + int(cur_char)
                else:
                    return 0
            case 0:
                if cur_char == " ":
                    lvl = 0
                elif cur_char == "+" or cur_char == "-":
                    lvl = 1
                    val = -1 if cur_char == "-" else 1
                elif cur_char.isdigit():
                    lvl = 2
                    y = y*10 + int(cur_char)
                else:
                    return 0
        i += 1
    y = y * val
    y = min(y,2**31-1)
    y = max(y,-(2**31))       
    return y




if __name__ == __name__ :
    s = "wer 1"
    print (mya(s))