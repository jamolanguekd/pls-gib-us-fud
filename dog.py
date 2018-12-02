from gameobject import GameObject
import resources


class Dog(GameObject):
    def __init__(self, *args, **kwargs):
        super(Dog, self).__init__(img=resources.image_dog, *args, **kwargs)

        # ATTRIBUTES
        self.x = 0
        self.y = 0
        self.direction = None
        self.lane = None
        self.velocity_x = 100

        # FLAGS
        self.destroyed = False
        self.end = False
        self.fed = False

        # INITIAL VALUES
        self.set_direction("right")

    def check_end(self):
        if self.lane == 1:
            if self.x + self.width // 2 >= 665:
                self.velocity_x = 0
                self.end = True
        if self.lane == 2:
            if self.x + self.width // 2 >= 665:
                self.velocity_x = 0
                self.end = True
        if self.lane == 3:
            if self.x + self.width // 2 >= 655:
                self.velocity_x = 0
                self.end = True

    def check_home(self):
        if self.lane == 1:
            if self.x <= 170:
                self.destroyed = True

        if self.lane == 2:
            if self.x <= 190:
                self.destroyed = True

        if self.lane == 3:
            if self.x <= 190:
                self.destroyed = True

    def handle_collision(self, other_object):
        if not self.fed:
            if other_object.__class__.__name__ == "DogFood":
                if other_object.destroyed is False:
                    self.set_direction("left")
                    other_object.eaten = True
                    other_object.destroy()

    def set_direction(self, direction):
        self.direction = direction
        if self.direction == "right":
            self.image = resources.image_dog
        if self.direction == "left":
            self.fed = True
            self.image = resources.image_dog_reversed
            self.velocity_x = 500

    def set_lane(self, num):
        self.lane = num
        if self.lane == 1:
            self.x = 170
            self.y = 70

        if self.lane == 2:
            self.x = 190
            self.y = 185

        if self.lane == 3:
            self.x = 190
            self.y = 295

    def update(self, dt):
        super().update(dt)
        self.check_end()
        self.check_home()
