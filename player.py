from pyglet.window import key
from gameobject import GameObject
from dogfood import DogFood
import resources


class Player(GameObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.image_player, *args, **kwargs)
        self.x = 0
        self.y = 0
        self.velocity_x = 0.0
        self.direction = "none"
        self.lane = 1
        self.new_objects = []
        self.event_handlers = [self.on_key_press]

        self.set_lane(1)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.set_lane(self.lane+1)

        if symbol == key.DOWN:
            self.set_lane(self.lane-1)

        if symbol == key.Q:
            self.throw_dog_food()
            resources.music_throw.play()

    def throw_dog_food(self):
        new_food = DogFood(batch=self.batch)
        new_food.x = self.x
        new_food.y = self.y
        new_food.lane = self.lane
        self.new_objects.append(new_food)

    def set_lane(self, num):
        if 1 <= num <= 3:
            self.lane = num

        if num == 1:
            self.x = 665
            self.y = 70

        if num == 2:
            self.x = 665
            self.y = 185

        if num == 3:
            self.x = 655
            self.y = 295



