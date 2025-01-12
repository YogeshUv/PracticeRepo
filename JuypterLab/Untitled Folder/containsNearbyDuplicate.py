class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check = set()
        for i in range(k):
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])
        return False
    
s = Solution()
ans = s.containsNearbyDuplicate([1,2,3,1],3)
print(ans)
