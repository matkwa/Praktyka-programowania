class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    # bierze teraz imie ze zmiennej zamiast na sztywno player1
    def won_point(self, player_name):
        if player_name == self.player1_name :
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1

    #rozbicie na mniejsze elementy zamiast zagniezdzonych if else
    def score(self):
        if self.p1points == self.p2points:
            return self._get_tied_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()


    def _get_tied_score(self):
        score_names = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        return score_names.get(self.p1points, "Deuce")

    # zmienne zamiast sztywnych imion graczy
    def _get_advantage_or_win_score(self):
        score_difference = self.p1points - self.p2points
        
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    # usuniecie petli i zmiennej temp
    def _get_regular_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.p1points]}-{score_names[self.p2points]}"
