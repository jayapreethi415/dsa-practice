class Solution(object):
    def sortedSquares(self, nums):
        arr = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                arr[index] = nums[left] * nums[left]
                left += 1
                index -= 1
            else:
                arr[index] = nums[right] * nums[right]
                right -= 1
                index -= 1
        return arr


        