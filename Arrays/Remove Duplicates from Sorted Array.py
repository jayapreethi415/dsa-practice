class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        write = 2
        
        for read in range(2,len(nums)):
            current = nums[read]

            if current != nums[write - 2]:
                nums[write] = current
                write += 1

        return write