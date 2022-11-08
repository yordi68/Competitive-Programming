class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_heights = list(zip(names,heights))
        name_heights_sorted = sorted(name_heights,key=lambda x:x[1],reverse = True)
        return [names for names,heughts in name_heights_sorted]