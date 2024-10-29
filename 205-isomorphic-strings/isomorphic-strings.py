class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        lists=list(s)
        listt=list(t)
        dictionary={}
        for i,j in zip( lists,listt):
            if i in dictionary:
                if dictionary[i]!=j:
                    return False
            else:
                
              if j in dictionary.values():
                return False
              dictionary[i]=j        
        return True                