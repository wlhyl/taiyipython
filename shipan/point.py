def Get九宫Point(s):
    if not isinstance(s, int):
        raise ValueError("参数只能是整数")
    if s < 1 or s > 9:
        raise ValueError("九宫数是1-9")
    sToP = [0, JiuGongPoint(3, 3), JiuGongPoint(1, 2), JiuGongPoint(3, 1),
            JiuGongPoint(2, 1), JiuGongPoint(2, 2), JiuGongPoint(2, 3),
            JiuGongPoint(1, 3), JiuGongPoint(3, 2), JiuGongPoint(1, 1), ]
    return sToP[s]


def Get间辰Point(s):
    if not isinstance(s, str):
        raise ValueError("参数只能是字符串")
    pToN = {
        "巽": JianChenPoint(0, 0),
        "巳": JianChenPoint(0, 1),
        "午": JianChenPoint(0, 2),
        "未": JianChenPoint(0, 3),
        "坤": JianChenPoint(0, 4),
        "申": JianChenPoint(1, 4),
        "酉": JianChenPoint(2, 4),
        "戌": JianChenPoint(3, 4),
        "乾": JianChenPoint(4, 4),
        "亥": JianChenPoint(4, 3),
        "子": JianChenPoint(4, 2),
        "丑": JianChenPoint(4, 1),
        "艮": JianChenPoint(4, 0),
        "寅": JianChenPoint(3, 0),
        "卯": JianChenPoint(2, 0),
        "辰": JianChenPoint(1, 0),
    }
    p = pToN.get(s)
    if p is None:
        raise ValueError("无此{}宫".format(s))
    return p


class Point():
    points = []

    def __init__(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError('{}，{} 必须是整数'.format(x, y))
        if (x, y) not in self.points:
            raise ValueError("({},{})不在允许范围内".format(x, y))
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise ValueError("只能用于Point类型")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, Point):
            raise ValueError("只能用于Point类型")
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("被加数需要是整数")
        n = (self.points.index((self.__x, self.__y)) +
             other) % len(self.points)
        return self.points[n]

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError("只能用于Point类型")
        tmp = self.points.index((self.x, self.y)) - \
            self.points.index((other.x, other.y))
        return (tmp + len(self.points)) % len(self.points)

    def __str__(self):
        return "({},{})".format(self.__x, self.__y)


class JianChenPoint(Point):
    points = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4),
              (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0)]

    def __init__(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError('{}，{} 必须是整数'.format(x, y))
        super().__init__(x, y)

    @property
    def 宫数(self):
        if self.x == 0 and self.y == 0:
            return 9
        if self.x == 4 and self.y == 0:
            return 3
        if self.x == 4 and self.y == 4:
            return 1
        if self.x == 0 and self.y == 4:
            return 7
        if self.x == 0 and self.y == 2:
            return 2
        if self.x == 2 and self.y == 0:
            return 4
        if self.x == 4 and self.y == 2:
            return 8
        if self.x == 2 and self.y == 4:
            return 6
        return 0

    @property
    def 九宫Point(self):
        if (self.x == 0 and self.y == 0) or \
                (self.x == 1 and self.y == 0) or \
                (self.x == 0 and self.y == 1):
            return JiuGongPoint(1, 1)
        if (self.x == 4 and self.y == 0) or \
                (self.x == 3 and self.y == 0) or \
                (self.x == 4 and self.y == 1):
            return JiuGongPoint(3, 1)
        if (self.x == 4 and self.y == 4) or \
                (self.x == 4 and self.y == 3) or \
                (self.x == 3 and self.y == 4):
            return JiuGongPoint(3, 3)
        if (self.x == 0 and self.y == 4) or \
                (self.x == 0 and self.y == 3) or \
                (self.x == 1 and self.y == 4):
            return JiuGongPoint(1, 3)
        if self.x == 0 and self.y == 2:
            return JiuGongPoint(1, 2)
        if self.x == 2 and self.y == 0:
            return JiuGongPoint(2, 1)
        if self.x == 4 and self.y == 2:
            return JiuGongPoint(3, 2)
        if self.x == 2 and self.y == 4:
            return JiuGongPoint(2, 3)

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("被加数需要是整数")
        n = (self.points.index((self.x, self.y)) +
             other) % len(self.points)
        return JianChenPoint(self.points[n][0], self.points[n][1])


class JiuGongPoint(Point):
    points = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1),
              (2, 2)]

    def __init__(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError('{}，{} 必须是整数'.format(x, y))
        super().__init__(x, y)

    @property
    def 宫数(self):
        if self.x == 1 and self.y == 1:
            return 9
        if self.x == 1 and self.y == 2:
            return 2
        if self.x == 1 and self.y == 3:
            return 7
        if self.x == 2 and self.y == 3:
            return 6
        if self.x == 3 and self.y == 3:
            return 1
        if self.x == 3 and self.y == 2:
            return 8
        if self.x == 3 and self.y == 1:
            return 3
        if self.x == 2 and self.y == 1:
            return 4
        return 5

    @property
    def 间辰Point(self):
        a = JianChenPoint(0, 0)
        for i in range(0, 16):
            b = a + i
            if b.宫数 == self.宫数:
                return b
        # 在中宫返回九宫的位置
        return JiuGongPoint(2, 2)

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("被加数需要是整数")
        if self.x == 2 and self.y == 2:
            return JiuGongPoint(2, 2)
        points = self.points[0:len(self.points)-1]
        n = (points.index((self.x, self.y)) +
             other) % len(points)
        return JiuGongPoint(points[n][0], points[n][1])

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError("只能用于Point类型")
        points = self.points[0:len(self.points) - 1]
        tmp = points.index((self.x, self.y)) - points.index((other.x, other.y))
        return (tmp + len(points)) % len(points)


if __name__ == "__main__":
    p = JiuGongPoint(1, 1)
    p2 = JiuGongPoint(1, 2)
    print(p2 - p)
    print(JiuGongPoint(2, 2))
    # p1 = JianChenPoint(2, 0)
    # for i in range(0,18):
    #     print(type(p+i))
