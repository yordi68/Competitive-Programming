class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        result_winners = []
        result_losers = []
        dictionary = {}
        #creating a dictionary inorder to count the number of loses
        for winner,loser in matches:
            if winner not in dictionary:
                dictionary[winner] = 0
            if loser in dictionary:
                dictionary[loser] += 1
            else:
                dictionary[loser] = 1
        #if the dictionary values are 0 then they have not lost any matches
        # if the dictionary valus are 1 then they have lost exactly one matches
        for keys in dictionary:
            if dictionary[keys] == 0:
                result_winners.append(keys)
            elif dictionary[keys] == 1:
                result_losers.append(keys)

        return([sorted(result_winners),sorted(result_losers)])