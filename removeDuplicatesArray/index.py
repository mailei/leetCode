
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 参照アドレスの値を変更
        # a = 123
        # b = 111
        # c = a
        # c[:] = b
        #expect a == b 
        nums[:] = sorted(set(nums))
        return len(nums)
                      
