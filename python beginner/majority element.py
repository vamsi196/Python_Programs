class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        threshold=n//2
        result=[]
        for num in nums:
            count[num]=count.get(num,0)+1
            
            if count[num]>threshold:
                return num
        return -1
        