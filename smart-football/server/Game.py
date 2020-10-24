from Team import Team
import threading
from Connection import sendData, connection

TEAM_A = "A"
TEAM_B = "B"


class Game(threading.Thread):
    def __init__(self):
        super(Game, self).__init__()

        self.lock = threading.Condition()
        self.team_a = Team(self, TEAM_A, side = 50)
        self.team_b = Team(self, TEAM_B, side = 0)
        self.active_team = self.team_a
        self.time = 90
        self.score = {TEAM_A: 0, TEAM_B: 0}
        self.team_in_possession = TEAM_A
        # game ball
        self.ball_x = 50
        self.ball_y = 25

    def run(self):

        sendData("msg", "Game Started")
        sendData("game", self.get_game_data())

        while True:
            if connection.input_stack:
                print(connection.input_stack)
                msg, game_data = self.interpret_cmd(connection.input_stack.pop(0))
                sendData("msg", msg)
                sendData("game", game_data)


    # command interpretor
    def interpret_cmd(self, key):
        if key == "a":
            self.active_team = self.team_a
            msg = "Team A selected"
        elif key == "b":
            self.active_team = self.team_b
            msg = "Team B selected"
        else:
            msg = self.active_team.interpret_cmd(key)
        
        return msg, self.get_game_data()
    
    def get_game_data(self):
        data = {
            "ball": [self.ball_x, self.ball_y],
            "team_a": [[player.x,player.y] for player in self.team_a.players],
            "team_b": [[player.x,player.y] for player in self.team_b.players]
        }

        return data

    # game events
    def reset_field(self):
        self.team_a.reset_players()
        self.team_b.reset_players()
        self.ball_x = 0
        self.ball_y = 0

    def goal_scored(self, team_name):
        self.score[team_name] += 1
        self.reset_field()
    
    def set_ball_pos(self,coord):
        self.ball_x, self.ball_y = coord