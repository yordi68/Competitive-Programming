class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position,speed))
        position_speed.sort(key=lambda x:x[0])
        stack = []
        time =[(target-i)/v  for i,v in position_speed]
        count = 0
        for i in range(len(time)):
            while stack and stack[-1] <= time[i]:
                stack.pop()
            stack.append(time[i])

        return len(stack)