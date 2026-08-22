class Solution:
    def mySqrt(self, x: int) -> int:
        temp = 0
        if x == 0:
            return 0
        while temp * temp <= x:
            temp += 1
        return temp - 1