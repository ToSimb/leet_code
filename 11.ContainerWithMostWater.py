def maxArea(height: list[int]) -> int:
    maxHeight = 0
    for i in range(len(height)-1):
        for j in range(i + 1,len(height)):
            ans = min(height[i],height[j]) * (j-i)
            maxHeight = max(maxHeight,ans)
    return (maxHeight)

def maxArea2(height: list[int]) -> int:
    maxHeight = 0
    i,j = 0, len(height)-1
    while i < j:
        ans = min(height[i],height[j]) * (j - i)
        maxHeight = max(maxHeight,ans)

        if height[j] > height[i]:
            i += 1
        else:
            j -= 1
    return (maxHeight)



if "__name__" == "__name__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea2(height))