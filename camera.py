from vector import Vector


class Camera:

    def __init__(self):
        self.position = Vector(-5,-2)
        self.scale = 0.25#0.4#0.50
        self.size = Vector(1000,600)
        self.time_per_day = 0.5


    def transform_position(self, pos):
        transformed = ((pos - self.position) / self.scale)
        flipped = Vector(transformed.x, self.size.y - transformed.y)
        return flipped

    def update_position(self, elapsed_time):
        self.position += Vector(1,0) * (elapsed_time / self.time_per_day)
        #pass # self.position += elapsed_time / self.time_per_day
