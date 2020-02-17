class Stats:
    def __init__(self, g_set):
        self.g_set = g_set
        self.game_on = False
        self.h_points = 0
        self.reset_stat()


    def reset_stat(self):
        self.s_left = self.g_set.s_limit
        self.points = 0
        self.level = 1

