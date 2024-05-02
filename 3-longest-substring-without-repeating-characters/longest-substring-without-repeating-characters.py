class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        left = 0
        maxLength = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1
            
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength