from Team import Team

TEAM_A = 'A'
TEAM_B = 'B'

class Game():
    def __init__(self):
        self.team_a = Team(self,TEAM_A)
        self.team_b = Team(self,TEAM_B)
        self.time = 90
        self.score = {
            TEAM_A: 0,
            TEAM_B: 0
        }
        self.team_in_possession = TEAM_A

        # game ball
        self.ball_x = 0
        self.ball_y = 0

    # game events
    def reset_field(self):
        self.team_a.reset_players()
        self.team_b.reset_players()
        self.ball_x = 0
        self.ball_y = 0
        pass

    def goal_scored(self, team_name):
        self.score[team_name] += 1
        self.reset_field()
        pass

