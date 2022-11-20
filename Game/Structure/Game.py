from events import Events

class Game():
    def __init__(self):
        self.events = Events()

    def update(self):
        self.events.onUpdate()

    def subscribeToUpdate(self, objMethod):
        self.events.onUpdate += objMethod
