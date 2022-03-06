from manim import *
from Point import *
from Triangle import *

class testTriangle(Scene):
    def construct(self):
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-6.0, 6.0, 1))
        self.add(grid)
        p1 = Point.Point(2, 3)
        p2 = Point.Point(4, -1)
        p3 = Point.Point(1, 1)
        a = Line(p1.to_list(), p2.to_list())
        a.append_points(Line(p2.to_list(), p3.to_list()).points)
        a.append_points(Line(p3.to_list(), p1.to_list()).points)
        t = Triangle(p1, p2, p3)
        b = Line(t.a.to_list(), t.b.to_list())
        b.append_points(Line(t.b.to_list(), t.c.to_list()).points)
        b.append_points(Line(t.c.to_list(), t.a.to_list()).points)
        d = t.denorm(t.a).to_list()
        e = t.denorm(t.b).to_list()
        f = t.denorm(t.c).to_list()
        c = Line(d, e)
        c.append_points(Line(e, f).points)
        c.append_points(Line(f, d).points)
        self.play(Create(grid, run_time=2, lag_ratio=0.1))
        self.play(Create(a))
        self.wait()
        self.play(Transform(a, b))
        self.wait()
        self.play(Transform(a, c))