import Point


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        norm_p1 = self.p1.copy()
        norm_p2 = self.p2.copy()
        norm_p3 = self.p3.copy()
        A = Point.distance(p2, p3)
        B = Point.distance(p1, p3)
        C = Point.distance(p1, p2)
        origin_point = p2
        reflect = p1

        if (A - B) * (C ** 2 - (A + B) ** 2) > 0:
            origin_point = p1
            reflect = p2
        rotate_by = ((p3.y - origin_point.y) / Point.distance(p3, origin_point),
                     (p3.x - origin_point.x) / Point.distance(p3, origin_point))
        rotate = lambda x, y: (rotate_by[1] * x + rotate_by[0] * y, -rotate_by[0] * x + rotate_by[1] * y)

        if rotate(reflect.x - origin_point.x, reflect.y - origin_point.y)[1] < 0:
            reflect = -1
        else:
            reflect = 1
        scale = 1 / rotate(p3.x - origin_point.x, p3.y - origin_point.y)[0]

        def transform(p: Point):
            newx = p.x - origin_point.x
            newy = p.y - origin_point.y
            newx, newy = rotate(newx, newy)
            newy *= scale
            newy *= scale * reflect
            return Point.Point(newx, newy)

        self.transform = transform

    def centroid(self):
        return Point.Point((self.p1.x + self.p2.x + self.p3.x) / 3, (self.p1.y + self.p2.y + self.p3.y) / 3)
