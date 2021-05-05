"""
Given a list of integers and a target value, return the indices of the two numbers in the
list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot
be used more than once.

Example:

Given nums = [3, 8, 12, 17], target = 15

because nums[0] + nums[2] = 3 + 12 = 15
return [0, 2]

Use a dictionary to add each number with it's index
nums = {3: 0, 8: 1, 12: 2, 17: 3}
"""

def two_sum(nums, target):
    # Your code here
    nums_dict = {} # initialize a dictionary to hold number as key, value as index
    result = [] # append index if the number is found in the dictionary

    for index, num in enumerate(nums):
        # add the nums to the dictionary with value as the index
        nums_dict[num] = index

    for num, value in nums_dict.items():
        # iterate through the dictionary
        # subtract the num from the target to get the other value needed
        new_target = target - num
        # if the new target is in the dictionary, append the index to the result list
        if new_target in nums_dict:
            result.append(value)

    if result == []:
        return -1
    else:
        return result



# nums = [1,1,1,1]
# target = 8
nums = 3, 8, 12, 17
target = 15

print(two_sum(nums, target))