from Players import Defender, Midfielder, Forward
import threading

class Team(threading.Thread):
    def __init__(self, game, team_name, side):
        super(Team, self).__init__()
        self.defenders = [
            Defender(team=self, start_x=35+(side), start_y=int(50 / 4 * i))
            for i in range(4)
        ]
        self.midfielders = [
            Midfielder(team=self, start_x=20+(side), start_y=int(50 / 3 * i))
            for i in range(3)
        ]
        self.forwards = [
            Forward(team=self, start_x=5+(side), start_y=int(50 / 3 * i))
            for i in range(3)
        ]
        self.players = self.defenders + self.midfielders + self.forwards
        self.active_player_indx = 0
        self.game = game
        self.name = team_name
        self.rating = 0.5
        # self.possession

    def run(self):
        for player in self.players:
            player.start()

    def interpret_cmd(self, key):
        if key in [str(i) for i in range(10)]:
            self.active_player_indx = int(key)
            msg = "Active player updated"
        elif key in ["p", "ArrowLeft", "ArrowRight", "ArrowDown", "ArrowUp"]:
            self.players[self.active_player_indx].manual_move(key)
            msg = "Player moved: " + key
        else:
            msg = "Unknown key"
        return msg


    def reset_players(self):
        for player in self.players:
            player.reset_position()


    def update_team_rating(self):
        score_sum = sum([score for team, score in self.game.score.items()])
        return min(1, self.game.score[self.name] / score_sum)
