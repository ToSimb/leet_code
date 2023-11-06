nums1 = [1,3]
nums2 = [2]

# functions
 # ручной Brute Forse
def searsh1 (nums1: list[int], nums2: list[int]) -> float:
    m =  len(nums1)
    n =  len(nums2)
    nums = []
    while len(nums1) != 0 and len(nums2) != 0 :
        if (nums1[0] < nums2[0]):
            nums.append(nums1[0])
            nums1.pop(0)
        else:
            nums.append(nums2[0])
            nums2.pop(0)
    while len(nums1) != 0:
        nums.append(nums1[0])
        nums1.pop(0)

    while len(nums2) != 0:
        nums.append(nums2[0])
        nums2.pop(0)

    print(nums)
    if (n+m) % 2 == 1:
        return nums[int((n+m)/2)]
    else:
        return (nums[int((n+m)/2 - 1)] + nums[int((n+m)/2)]) /2.0


 # Brute Forse
def searsh2 (nums1: list[int], nums2: list[int]) -> float:
    nums = nums1 + nums2
    n = len(nums)
    nums.sort()
    if n % 2 == 1:
        return nums[int(n/2)]
    else:
        return (nums[int(n/2-1)] + nums[int(n/2)]) /2.0
 # Two-Pointer Method
def searsh3 (nums1: list[int], nums2: list[int]) -> float:
    m =  len(nums1)
    n =  len(nums2)
    i1 = 0
    i2 = 0
    m1 = 0
    m2 = 0 

    for count in range(0, (n+m) // 2 + 1):
        m2 = m1
        if i1 < m and i2 < n:
            if (nums1[i1] < nums2[i2]):
                m1 = nums1[i1]
                i1 +=1
            else:
                m1 = nums2[i2]
                i2 +=1
        elif i1 < m:
            m1 = nums1[i1]
            i1 +=1
        else:
            m1 = nums2[i2]
            i2 +=1
    if (n+m) % 2 == 1:
        return float(m1)
    else:
        return (m1+m2)/2.0



#print(searsh1(nums1,nums2))
print(searsh3(nums1,nums2))