class Solution:
    def interpret(self, command: str) -> str:
        n = len(command) 
        res = ""
        
        for i in range(n):
            if command[i] == "G":
                res = res + "G" 
            elif command[i] == "(":
                if command[i + 1] == ")":
                    res = res + "o"
                elif command[i + 1].isalpha():
                    res = res + "al"
                    
        return res
                