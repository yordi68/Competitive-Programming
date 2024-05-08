class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score)
        hashmap = defaultdict(int)

        for i in range(len(sorted_score) - 1, -1, -1):
            hashmap[sorted_score[i]] = len(sorted_score) - i
            
        for i in range(len(score)):
            if hashmap[score[i]] == 1:
                score[i] = "Gold Medal"
            elif hashmap[score[i]] == 2:
                score[i] = "Silver Medal"
            elif hashmap[score[i]] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] =  f"{hashmap[score[i]]}"
        return score