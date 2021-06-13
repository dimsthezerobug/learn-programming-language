from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # self.all_players = []
    
    # def make_player(self):
    #     player = Turtle("turtle")
    #     player.speed(0)
    #     player.penup()
    #     player.goto(STARTING_POSITION)
    #     player.left(90)
    #     self.all_players.append(player)
    
    # def move_player(self):
    #     for player in self.all_players:
    #         if player.ycor() == 300:
    #             self.make_player()
    #         if player.ycor() > 300:
    #             self.all_players.remove(player)
    #         player.forward(MOVE_DISTANCE)
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
