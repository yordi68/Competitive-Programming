class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = min(skill) + max(skill)
        left = 0
        right = len(skill) - 1
        chem = 0
        while left < right:
            if skill[left] + skill[right] == total_skill:
                chem += (skill[left] * skill[right])
            else:
                return - 1
            left += 1
            right -= 1
            
        return chem