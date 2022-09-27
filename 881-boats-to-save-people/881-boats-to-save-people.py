class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        sum = 0
        l , r = 0 , len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            sum += 1
        return(sum)