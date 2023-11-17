sss = ""


# functions
 # ручной Brute Forse
def search1 ( s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxLen = 1
        maxStr = s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > maxLen and s[i:j+1] == s[i:j+1][::-1]:
                    maxLen = j-i+1
                    maxStr = s[i:j+1]

        return maxStr

 # поиск через центр
def search2 ( s: str) -> str:
        if len(s) <= 1:
            return s

        def center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        maxStr = s[0]
        for i in range(len(s) - 1):
            xx = center(i, i)
            xy = center(i, i + 1)

            if len(xx) > len(maxStr):
                maxStr = xx
            if len(xy) > len(maxStr):
                maxStr = xy

        return maxStr

print(search2(sss))