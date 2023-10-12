class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            part = queryIP.split('.')
            if len(part) != 4:
                return "Neither"
            for i in range(len(part)):
                if (len(part[i]) > 1 and part[i][0] == '0' ) or (not part[i].isdigit()):
                    return "Neither"
                if int(part[i]) > 255:
                    return "Neither"
                
            return "IPv4"
            
                
        elif ':' in queryIP:
            part = queryIP.split(':')
            if len(part) != 8:
                return "Neither"
            for i in range(len(part)):
                if not (0 < len(part[i]) < 5):
                    return "Neither"
                for j in part[i].lower():
                    if j.isdigit():
                        continue
                        
                    if not (ord('a') <= ord(j) <= ord('f')):
                        
                        return "Neither"
            return "IPv6"
            
        else:
            return "Neither"
        