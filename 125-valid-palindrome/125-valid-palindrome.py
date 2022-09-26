class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_string = ''.join(char for char in s.lower() if char.isalnum())
        return updated_string == updated_string[::-1]