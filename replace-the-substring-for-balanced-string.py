class Solution:
    def balancedString(self, s: str) -> int:
        s_count = Counter(s)
        count = len(s) // 4
        refHash = defaultdict(int)

        for key in s_count:
            diff = s_count[key] - count
            if diff > 0:
                refHash[key] += diff
        
        left = 0
        counter = 0
        window = defaultdict(int)
        length = float("inf")
        
        for right in range(len(s)):
            
            if s[right] in refHash:
                window[s[right]] += 1
                if window[s[right]] == refHash[s[right]]:
                    counter += 1

            while counter and counter == len(refHash):
                length = min(length,right - left + 1)
                
                if s[left] in refHash:
                    window[s[left]] -= 1

                    if window[s[left]] < refHash[s[left]]:
                        counter -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                left += 1

        return length if length != float("inf") else 0