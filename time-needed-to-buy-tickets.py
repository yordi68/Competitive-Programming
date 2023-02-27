class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        pairs = list(enumerate(tickets))
        que = deque(pairs)
        time = 0

        while len(que) != 0:
            x , y = que.popleft()
            y -= 1
            if y > 0:
                que.append(tuple([x,y]))
            if y == 0 and x == k:
                return time + 1

            time += 1