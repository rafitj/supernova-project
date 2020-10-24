import random
import math
import threading

# abstract player class
class Player(threading.Thread):
    def __init__(self, team, start_x, start_y):
        super(Player, self).__init__()

        self.team = team
        self.lock = threading.Condition()

        # player stats (out of 100)
        self.speed: int = 50
        self.shooting: int = 50
        self.passing: int = 50
        self.physical: int = 50
        self.defending: int = 50
        self.dribbling: int = 50

        # coordinates
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.x: int = start_x
        self.y: int = start_y
        self.has_ball: bool = False

        #  game stats
        self.rating: float = 0
        self.attempted_passes: int = 0
        self.succesful_passes: int = 0
        self.attempted_shots: int = 0
        self.succesful_shots: int = 0
        self.attempted_dribbles: int = 0
        self.succesful_dribbles: int = 0
        self.attempted_tackles: int = 0
        self.succesful_tackles: int = 0
        self.goals_scored: int = 0

        # future stats
        self.vision = 20
        # self.strength
        # self.jump
        # self.crossing
        # self.interception

    def run(self):
        # with self.lock:
        #     self.lock.wait()
        # self.ride()
        pass
    
    def manual_move(self, key):
        if key == 'ArrowUp':
            self.y -= 1
        elif key == 'ArrowDown':
            self.y += 1
        elif key == 'ArrowLeft':
            self.x -= 1
        elif key == 'ArrowRight':
            self.x += 1
        elif key == 'p':
            self.pass_ball()
        self.player_position_update()
    
    def player_position_update(self):
        if self.has_ball:
            self.team.game.ball_y = self.y
            self.team.game.ball_x = self.x
        elif self.team.game.ball_x == self.x and self.team.game.ball_y == self.y:
            self.has_ball = True

    def player_move(self, stat, attempted_stat, succesful_stat):
        # roll = random.randint(0, 100) * (stat / 100)
        is_succesful_move = True
        attempted_stat += 1
        if is_succesful_move:
            self.has_ball = True
            succesful_stat += 1
        self.update_rating()

    def shoot(self):
        pass

    def tackle(self):
        if not self.has_ball:
            self.player_move(
                self.defending, self.attempted_tackles, self.succesful_tackles
            )

    def dribble(self):
        if self.has_ball:
            self.player_move(
                self.dribbling, self.attempted_dribbles, self.succesful_dribbles
            )

    def move_player(self):
        # if ball make move
            
        # if opposing player make move

        pass
    
    def in_view(self,x,y):
        distance = math.sqrt(((x-self.x)**2)+((y-self.y)**2))
        return distance <= self.vision

    def pass_ball(self):
        if self.has_ball:
            pass_options = [(player.x,player.y) for player in self.team.players if self.in_view(player.x,player.y) and not (player.x == self.x and player.y == self.y)]
            if pass_options:
                pass_coords = pass_options[0]
                self.team.game.set_ball_pos(pass_coords) 
                self.has_ball = False
    
    def update_rating(self):
        pass_rating = self.succesful_passes / self.attempted_passes
        dribble_rating = self.succesful_dribbles / self.attempted_dribbles
        shot_rating = self.succesful_shots / self.attempted_shots
        tackle_rating = self.succesful_tackles / self.attempted_tackles
        team_rating = self.team.rating
        goal_rating = max(self.goals_scored / 3, 3)

        self.rating = (
            (pass_rating * 0.15)
            + (dribble_rating * 0.15)
            + (shot_rating * 0.15)
            + (tackle_rating * 0.15)
            + (team_rating * 0.3)
            + (goal_rating * 0.1)
        )

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y


# player types
class Defender(Player):
    def __init__(self, team, start_x, start_y):
        super().__init__(team, start_x, start_y)
        self.physical: int = 80
        self.defending: int = 80


class Midfielder(Player):
    def __init__(self, team, start_x, start_y):
        super().__init__(team, start_x, start_y)
        self.passing: int = 80
        self.defending: int = 60
        self.shooting: int = 65
        self.speed: int = 70
        self.dribbling: int = 80


class Forward(Player):
    def __init__(self, team, start_x, start_y):
        super().__init__(team, start_x, start_y)
        self.passing: int = 60
        self.defending: int = 30
        self.shooting: int = 80
        self.speed: int = 75
        self.dribbling: int = 70
        self.physical: int = 70
