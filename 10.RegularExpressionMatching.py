# Recursion
def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    first = bool(s) and p[0] in [s[0], "."]
    if len(p) > 1 and p[1] == "*":
        return isMatch(s,p[2:]) or (first and isMatch(s[:1],p))
    else:
        return first and isMatch(s[1:],p[1:])


if "__name__" == "__name__":
    s = "asdd"
    p = "asc*d."
    print (isMatch(s, p))
