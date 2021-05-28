from typing import FrozenSet


def first_missing_positive(nums):
  # if empty list, return 1
  if not nums:
    return 1

  # run through list to move valid values "v" to be located at index "v - 1"
  # relocate the value "v" (0 < v < length) from the current index to index "v - 1"
  # values outside of "0 < v < length" don't matter
  # swap values in the list so that index "v - 1" now holds current value "v"
  # the current index location will now hold the value that was swapped against
  # break out of while loop if current value and swapped value are the same
  for i, num in enumerate(nums):


    while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
      v = nums[i]
      nums[i], nums[v - 1] = nums[v - 1], nums[i]

      if nums[i] == nums[v - 1]:
        break #break out of while loop if current value and swapped value are the same

  for i, num in enumerate(nums,1):
    if num != i:
      return i

  return len(nums) + 1
