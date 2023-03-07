class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(s):
            i = 0
            res = ""
            while i < len(s):
                if s[i].isdigit():
                    num = ""
                    string = ""
                    count = 0
                    while i < len(s) and s[i] != '[':
                        num += s[i]
                        i += 1
                    count += 1
                    i += 1
                    while i < len(s) and count:
                        if s[i] == '[':
                            count += 1
                        if s[i] == ']':
                            count -= 1
                        string += s[i]
                        i += 1
                    i -= 1
                    
                    res += decode(string[:-1]) * int(num)
                    
                else:
                    res += s[i]

                i += 1
            return res
        
        return decode(s)