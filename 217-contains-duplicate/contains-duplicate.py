class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for number in nums:
            
            if number in seen:
                return True
            else:
                seen.add(number)
        
        return False

        