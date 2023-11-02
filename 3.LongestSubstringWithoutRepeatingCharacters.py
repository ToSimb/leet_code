# parameters
s = "ad dacdcc"

# functions
    # Brute Forse
def searsh1 (s: str) -> int:
    n = len(s)
    maxLen = 0

    for i in range(n):
        charSet = set()
        charSet.add(s[i])
        j = i+1
        iLen = 1
        while (j < n) and (s[j] not in charSet)  :
            charSet.add(s[j])
            j += 1
            iLen += 1
        maxLen = max(maxLen, iLen)  

    return maxLen
    # через 2 каретки 
def searsh2 (s: str) -> int:
    n = len(s)
    charSet = set()
    maxLen = 0
    left = 0

    for right in range(n):
        if s[right] not in charSet:
            charSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)  
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])

    return maxLen
    # Unordered Map
def searsh3 ( s: str) -> int:
        n = len(s)
        maxLen = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLen = max(maxLen, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLen
    # Integer Array
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    maxLength = 0
    charIndex = [-1] * 128
#    print (charIndex)

    left = 0
        
    for right in range(n):
        if charIndex[ord(s[right])] >= left:
            left = charIndex[ord(s[right])] + 1

        charIndex[ord(s[right])] = right
        maxLength = max(maxLength, right - left + 1)
#    print (charIndex)
    return maxLength

# вывод
print (searsh1(s))
print (searsh2(s))
print (searsh3(s))
print (lengthOfLongestSubstring(s))
