from functools import singledispatch


class Shape(object):
    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):
    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Triangle(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

# dont use it on methods defined inside class as its first argument is self
# that is not possible to provided here

@singledispatch
def draw(shape): # now drow become and decorater
    raise TypeError(f"Don't Know How To Draw {shape}")


@draw.register(Circle)  # it will bing this function to object of type Circle
def draw_circle(shape):  # Now name of this function doesn't matter you can set is to _ for all such function
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def draw_parallelogram(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def draw_triangle(shape):
    print("\u25B2" if shape.solid else "\u25B3")


if __name__ == '__main__':
    shapes = [Circle((0, 0), radius=10, solid=True),
              Parallelogram(pa=(5, 6), pb=(6,7), pc=(2,3), solid=False),
              Triangle(pa=(5, 6), pb=(6,7), pc=(2,3), solid=True)]

    for shape in shapes:
        draw(shape)