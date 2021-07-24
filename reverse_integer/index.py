
class Solution:
    def reverse(self, x: int) -> int:
        mozi = str(x)
        ans = 0
        if x < 0:
            ans = int(mozi[:0:-1]) * -1
        else:
            ans = int(mozi[::-1])

        if -2 ** 31 > ans or ans > 2 ** 31:
            return 0
        return ans

