from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """
    Function to perform binary search on a sorted list.
    
    Parameters:
    nums (List[int]): The sorted list to search.
    target (int): The target value to find.
    
    Returns:
    int: The index of the target if found, otherwise the index where it can be inserted.
    """
    if not nums:
        raise ValueError("Input list is empty")

    def search(l: int, r: int) -> int:
        """
        Recursive function to perform the binary search.
        
        Parameters:
        l (int): The left index of the search range.
        r (int): The right index of the search range.
        
        Returns:
        int: The index of the target if found, otherwise the index where it can be inserted.
        """
        if l > r:
            return l
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return search(l, mid - 1)
        else:
            return search(mid + 1, r)

    return search(0, len(nums) - 1)


nums = [1,3,5,6]
target = 5

assert searchInsert(nums, target) == 2