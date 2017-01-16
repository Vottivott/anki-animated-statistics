from vector import Vector


class Camera:

    def __init__(self):
        self.position = Vector(-2,-2)
        self.scale = 0.4#0.50
        self.size = Vector(1000,600)


    def transform_position(self, pos):
        transformed = ((pos - self.position) / self.scale)
        flipped = Vector(transformed.x, self.size.y - transformed.y)
        return flipped

    def update_position(self, elapsed_time):
        pass # self.position += elapsed_time / self.time_per_day
