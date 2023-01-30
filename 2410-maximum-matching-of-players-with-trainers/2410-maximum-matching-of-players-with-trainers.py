class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = 0
        right = 0
        player_len = len(players)
        trainer_len =len(trainers)
        count = 0
        while left < player_len and right < trainer_len:
            if trainers[right] >= players[left]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
                
        return count