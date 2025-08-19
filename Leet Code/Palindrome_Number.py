class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  #negative numbers are never palindromes

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10               #take the last digit
            reversed_num = reversed_num * 10 + digit  #append digit
            x //= 10                     #remove the last digit

        return original == reversed_num
