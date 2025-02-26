from typing import List


def swap(nums: List[int], index_one: int, index_two: int):
    nums[index_one], nums[index_two] = nums[index_two], nums[index_one]


def multiply(nums: List[int], index_one: int, index_two: int):
    """Takes element at the 1st index and multiply it with the element at 2nd index.
    Save the product at the 1st index."""
    nums[index_one] *= nums[index_two]


def decrease(nums: List[int]):
    """Decreases all elements in the array with 1."""
    return [num - 1 for num in nums]


def array_modifier(nums):
    while True:
        command = input()

        if command == 'end':
            return ', '.join(map(str, nums))

        parts = command.split()
        action = parts[0]

        if action == 'swap':
            swap(nums, int(parts[1]), int(parts[2]))

        elif action == 'multiply':
            multiply(nums, int(parts[1]), int(parts[2]))

        elif action == 'decrease':
            nums = decrease(nums)


numbers = list(map(int, input().split()))
result = array_modifier(numbers)
print(result)
