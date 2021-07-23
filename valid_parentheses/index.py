
class Solution:
    def isValid(self, s: str) -> bool:
        ans=False
        dic = {"(":")", "{":"}", "[":"]"}
        stack = []
        for mozi in s:
            if mozi in dic.values() and (len(stack) > 0 and dic[stack.pop()] == mozi):
                ans = True
            elif mozi in dic.keys():
                ans = False
                stack.append(mozi)
            else:
                ans = False
                break
        if len(stack) != 0:
            ans = False           
                
        return ans
                

