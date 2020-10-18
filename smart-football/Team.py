from Players import Defender, Midfielder, Forward


class Team:
    def __init__(self, game, team_name, side=1):
        self.defenders = [
            Defender(team=self, start_x=side * 35, start_y=int(50 / 4 * i))
            for i in range(4)
        ]
        self.midfielders = [
            Midfielder(team=self, start_x=side * 20, start_y=int(50 / 3 * i))
            for i in range(3)
        ]
        self.forwards = [
            Forward(team=self, start_x=side * 5, start_y=int(50 / 3 * i))
            for i in range(3)
        ]
        self.players = self.defenders + self.midfielders + self.forwards
        self.game = game
        self.name = team_name

    def reset_players(self):
        for player in self.players:
            player.reset_position()