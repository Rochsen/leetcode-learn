"""
896. 单调数列
如果数组是单调递增或单调递减的，那么它是 单调 的。

如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。

当给定的数组 nums 是单调数组时返回 true，否则返回 false。
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return self.isIncreasing(A) or self.isDecreasing(A)
        
    def isIncreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] < 0:
                return False
        return True
    
    def isDecreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] > 0:
                return False
        return True
    
    # check_up = True
    # check_down = True

    # for i in range(len(nums)-1):
    #     tmp_check_up = nums[i] <= nums[i+1]
    #     tmp_check_down = nums[i] >= nums[i+1]

    #     if tmp_check_up and check_up:
    #         check_up = True
    #     else:
    #         check_up = False
        
    #     if tmp_check_down and check_down:
    #         check_down = True
    #     else:
    #         check_down = False

    # return any((check_up, check_down))
