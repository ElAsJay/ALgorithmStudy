# 연습문제 6-1, 6-2
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def setx(self, x):
        self.X = x
    def sety(self, y):
        self.Y = y
    def get(self):
        print('('+str(self.X)+','+str(self.Y)+')')
    def move(self, dx, dy):
        self.X += dx
        self.Y += dy

point = Point(0,0)
point.get()
point.setx(3)
point.sety(2)
point.move(5, -5)
point.get()