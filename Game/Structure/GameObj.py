
from . import Game

class GameObj():
    def __init__(self, game:Game):
        self.game = game
        self.game.subscribeToUpdate(self.update)

    def update(self):
        print('Game Object Updated')
        return
