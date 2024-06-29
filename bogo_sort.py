import random

l=[4,5,6,9,5,3,5]

def bogosort(nums):
    
    def isSorted(l):
        if len(l) < 2:
            return True
        for i in range(len(l) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    while not isSorted(nums):
        random.shuffle(nums)
    return nums
print(bogosort(l))