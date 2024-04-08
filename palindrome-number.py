class Solution:
    def isPalindrome(self, x: int) -> bool:
            if x < 0:
                return False

            res = 0
            copy = x

            while x != 0:
                rem = x % 10
                res = res * 10 + rem
                x //= 10

            return copy == res

