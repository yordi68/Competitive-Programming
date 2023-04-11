"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = defaultdict(list)
        subordinates = defaultdict(list)
        
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates
            
        cnt = 0
        def dfs(subordinates, key):
            nonlocal cnt
            cnt += importance[key]

            for value in subordinates[key]:
                dfs(subordinates , value) 

        dfs(subordinates, id)
        return cnt