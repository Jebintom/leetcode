class Solution(object):
    def containsDuplicate(self, nums):
   
        dict={}
        for i,j in enumerate(nums):
            if j in dict:
                return True
            else:
                dict[j]=i
        return False    
        
        