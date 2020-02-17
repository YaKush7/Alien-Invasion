class Settings:

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.bgc = (230, 230, 230)
        self.title = "Test 1"

        # self.ship_speed = 1.5
        self.s_limit = 3

        # self.shoot_speed = 3
        self.shoot_height = 15
        self.shoot_width = 3
        self.shoot_limit = 5
        self.shoot_color = 60, 60, 60

        # self.ufo_speed = 1
        self.ufo_drop = 10
        # self.ufo_direct = -1

        self.speed_up = 1.1
        self.reset_speed()


    def reset_speed(self):
        self.ship_speed = 1.5
        self.shoot_speed = 3
        self.ufo_speed = 1
        self.ufo_direct = -1
        self.ufo_points = 50

    def inc_speed(self):
        self.ship_speed *= self.speed_up
        self.shoot_speed *= self.speed_up
        self.ufo_speed *= self.speed_up
