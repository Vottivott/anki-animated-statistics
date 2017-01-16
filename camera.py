from vector import Vector


class Camera:

    def __init__(self):
        self.position = Vector(-25,-20)
        self.scale = 0.65#0.3#0.25#0.4#0.50
        # self.size = Vector(1000,600)
        self.time_per_day = 0.1


    def transform_position(self, pos, window_size):
        transformed = ((pos - self.position) / self.scale)
        flipped = Vector(transformed.x, window_size.height() - transformed.y)
        return flipped

    def update_position(self, elapsed_time):
        self.position += Vector(1,0) * (elapsed_time / self.time_per_day)
        #pass # self.position += elapsed_time / self.time_per_day
