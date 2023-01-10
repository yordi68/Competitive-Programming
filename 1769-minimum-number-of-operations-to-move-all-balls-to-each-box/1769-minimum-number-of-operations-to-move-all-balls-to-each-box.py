class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = set()
        n = len(boxes)
        for i in range(n):
            if int(boxes[i]) == 1:
                ones.add(i)
        answer = [0] * n
        for i in range(n):
            total = 0
            for num in ones:
                total += abs(num - i)
            answer[i]= (total) 

        return answer

