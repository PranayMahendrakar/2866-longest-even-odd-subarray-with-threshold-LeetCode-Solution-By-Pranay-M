class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        max_len = 0
        i = 0
        while i < n:
            # Find a valid starting point (even and <= threshold)
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j-1] % 2:
                    length += 1
                    j += 1
                max_len = max(max_len, length)
                i = j
            else:
                i += 1
        return max_len