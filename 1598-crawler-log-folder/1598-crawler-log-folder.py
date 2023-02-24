class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for command in logs:
            if stack and command == "../":
                stack.pop()
            elif command != "./" and  command != "../":
                stack.append(command)

        return len(stack)
