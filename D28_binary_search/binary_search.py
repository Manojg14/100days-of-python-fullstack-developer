class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
        return -1


solution = Solution()
nums = [-1,0,3,5,9,12]
target = 12
print(solution.search(nums, target))



