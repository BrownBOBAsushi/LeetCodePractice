class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #     return False

        # Hash Set
        seen = set()

        for number in nums:
            seen.add(number)
            if number in seen:
                return True

        return False