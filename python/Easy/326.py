"""
326. Power of Three

给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
"""
class Solution:
    """不使用循环或递归的解法, n的范围 -2^31 <= n <= 2^31 - 1"""
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


class Solution:
    """递归解法"""
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


class Solution:
    """类似的解法"""
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


class Solution:
    """个人解法"""
    def isPowerOfThree(self, n: int) -> bool:
        tmp = 1

        while tmp < n:
            tmp *= 3
        
        return n == tmp


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(27))