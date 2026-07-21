#

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        phone={'2':"abc",
                '3':"def",
                '4':"ghi",
                '5':"jkl",
                '6':"mno",
                '7':"pqrs",
                '8':"tuv",
                '9':"wxyz",
                
                     }
        def bt(i,path):
            if i==len(digits):  #if the index ==len then path is added
                res.append(path)
                return
            for v in phone[digits[i]]:
                bt(i+1,path+v)
        bt(0,"") #starting from the 0 index and empty string
        return res
