

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width = 2
        )

class Cell():

    def __init__(self, win, 
                 has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        fill_color = "black"
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        me_x = 0.5*(self.__x1 + self.__x2)
        me_y = 0.5*(self.__y1 + self.__y2)
        to_x = 0.5*(to_cell.__x1 + to_cell.__x2)
        to_y = 0.5*(to_cell.__y1 + to_cell.__y2)
        if undo == False:
            fill_color = "red"
        else:
            fill_color = "gray"
        line = Line(Point(me_x, me_y),Point(to_x, to_y))
        self.__win.draw_line(line, fill_color)