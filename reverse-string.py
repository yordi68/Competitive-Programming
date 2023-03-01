class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(s,left,right):

            if left >= right:
                return s

            s[left] , s[right] = s[right] , s[left]
            return rev(s,left + 1,right - 1)

        return rev(s,0,len(s) - 1)