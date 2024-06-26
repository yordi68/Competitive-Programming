class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for chr in tokens:
            if chr == "+":
                stack.append(stack.pop() + stack.pop())

            elif chr == "-":
                last, second_last = stack.pop(), stack.pop()
                stack.append(second_last - last)

            elif chr == "*":
                stack.append(stack.pop() * stack.pop())

            elif chr == "/":
                last, second_last = stack.pop(), stack.pop() 
                stack.append(int(second_last / last))

            else:
                stack.append(int(chr))


        return stack[0]