Class TennisGame3:
    def __init__(self, player1_name, player2_name):
        # jasne nazwy zmiennych
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        #porównanie z faktyczną nazwą gracza
        if player_name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        # zachowanie kolejnosci ale bardziej czytelne czytelnym formatowaniem lepsze nazwy zmiennych usuniecie niepotrzebnego s
        if self.p1_points < 4 and self.p2_points < 4 and self.p1_points + self.p2_points < 6:
            score_names = ["Love", "Fifteen", "Thirty", "Forty"]
            p1_score = score_names[self.p1_points]
            return f"{p1_score}-All" if self.p1_points == self.p2_points else f"{p1_score}-{score_names[self.p2_points]}"
        
        if self.p1_points == self.p2_points:
            return "Deuce"
        
        #zastąpienie mnożenia funkcją abs()
        leader = self.player1_name if self.p1_points > self.p2_points else self.player2_name
        result_type = "Advantage" if abs(self.p1_points - self.p2_points) == 1 else "Win for"
        return f"{result_type} {leader}"
