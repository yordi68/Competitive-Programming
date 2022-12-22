class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary) - 2
        running_sum = 0
        for i in range(1,len(salary) - 1):
            running_sum += salary[i]
            
        return(running_sum / n)
            