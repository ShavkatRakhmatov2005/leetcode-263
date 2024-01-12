class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lst=[]
        dct={}
        for i in range(len(nums)):
            if (nums[i] in dct):
                dct[nums[i]]+=1
            else:
                dct[nums[i]]=1
        for j in dct.keys():
            if dct[j]>(len(nums)/3):
                lst.append(j)

        return lst


      
