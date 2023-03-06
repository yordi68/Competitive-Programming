class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        window = defaultdict(int)
        left = 0
        count = 0
        res = ""

        for right in range(len(s)):

            if s[right] in t_count:
                window[s[right]] += 1

                if t_count[s[right]] == window[s[right]]:
                    count += 1

            while count == len(t_count):
                if not res or (right - left + 1) < len(res):
                    res = s[left:right + 1]
                if s[left] in t_count:
                    window[s[left]] -= 1

                    if window[s[left]] < t_count[s[left]]:
                        count -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                left += 1

        return "".join(list(res))