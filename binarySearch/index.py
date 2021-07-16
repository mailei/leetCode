class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        # length が１の場合         
        if length == 1:
            return 0 if nums[0] >= target else 1
        return self.__binarySearch(nums, target, 0, length-1 )
    
    def __binarySearch(self, nums: List[int], target:int, start: int, end: int) -> int:
        # 終了条件
        if start > end:
            return start
        
        # 切り捨て
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid]  > target:
            return self.__binarySearch(nums, target, start, mid-1) 
        else:
            return self.__binarySearch(nums, target, mid + 1, end)
            
            
