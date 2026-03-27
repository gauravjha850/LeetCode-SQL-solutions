class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n=len(nums1)
        if min(nums1)%2!=0:
            return True
        else:
            ans = True
            nums1.sort()
            for i in range(0,n):
                if nums1[i]%2 !=0:
                    ans = False 
                    break              
            
            return ans
                