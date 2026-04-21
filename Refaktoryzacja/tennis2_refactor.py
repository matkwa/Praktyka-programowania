class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, name):
        # Dynamiczne sprawdzanie nazwy zamiast sztywnych stringów 
        if name == self.player1_name:
            self.p1_points += 1
        elif name == self.player2_name:
            self.p2_points += 1

    def score(self):
        # mapowanie punktów na nazwy zamiast if else

        point_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        
        #  tie
        if self.p1_points == self.p2_points:
            return "Deuce" if self.p1_points >= 3 else f"{point_names[self.p1_points]}-All"

        # advantage lub win
        if self.p1_points >= 4 or self.p2_points >= 4:
            diff = self.p1_points - self.p2_points
            leader = self.player1_name if diff > 0 else self.player2_name
            status = "Advantage" if abs(diff) == 1 else "Win for"
            return f"{status} {leader}"

        # normal score 
        return f"{point_names[self.p1_points]}-{point_names[self.p2_points]}"

# usuniete niepotrzebne funkcje p_score i p_set_score
