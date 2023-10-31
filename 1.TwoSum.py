# parameters
nums = [2,7,11,15]
target = 9

# functions
    # Brute Forse
def twoSum1(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]  

    # Hash Table
def twoSum2(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        a = target - nums[i]
        if a in hashmap:
            return [i, hashmap[a]]
        hashmap[nums[i]] = i


print(twoSum1(nums,target))
print(twoSum2(nums,target))