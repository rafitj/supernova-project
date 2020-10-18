import random

# abstract player class
class Player:
    def __init__(self, team, start_x, start_y):
        self.team = team

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
        # self.vision
        # self.strength
        # self.jump
        # self.crossing
        # self.interception

    def player_move(self, stat, attempted_stat, succesful_stat):
        roll = random.randint(0, 100) * (stat / 100)
        is_succesful_move = contend(roll)
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
        pass

    def dribble(self):
        if self.has_ball:
            self.player_move(
                self.dribbling, self.attempted_dribbles, self.succesful_dribbles
            )

    def run(self):
        # if ball make move

        # if opposing player make move
        pass

    def pass_ball(self):
        pass

    def update_rating(self):
        pass

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y
        pass


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
