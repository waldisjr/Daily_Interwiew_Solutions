import math


def products(nums):
    result = []
    for i in nums:
        copy_nums = nums.copy()
        copy_nums.remove(i)
        result.append(math.prod(copy_nums))
    return result


print(products([1, 2, 3, 4, 5]))
