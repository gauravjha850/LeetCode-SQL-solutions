class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=min(nums1)

        if all(x%2==0 for x in nums1) or all(x%2!=0 for x in nums1):
            return True
        return mn%2==1
        


                