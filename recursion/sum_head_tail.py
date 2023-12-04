""" Summing numbers in an array """

from typing import List
from functools import reduce
from time_it import time_it

def recurisve_sum(nums:List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        head = nums[0]
        tail = nums[1:]
        return head + recurisve_sum(tail)


@time_it
def iterative_sum(nums:List[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total

@time_it
def reduce_sum(nums:List[int]) -> int:
    return reduce(lambda x,y : x + y, nums)


arr= [1,2,3,4,5]
assert recurisve_sum(arr) == 15
assert recurisve_sum([1,2,3,4,5,6,7,8,9,10]) == 55


iterative_sum(arr)
reduce_sum(arr)
