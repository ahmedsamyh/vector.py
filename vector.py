import math
from math import *

class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set(self,x,y):
        self.x = x
        self.y = y

    def copy(self):
        return self

    def add(self, other):
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y

    def add(self, x=0, y=0):
        if isinstance(x, int) and isinstance(y, int):
            self.x += x
            self.y += y

    def sub(self, other):
        if isinstance(other, Vector2):
            self.x -= other.x
            self.y -= other.y

    def sub(self, x=0, y=0):
        self.x -= x
        self.y -= y

    def mult(self, other):
        if isinstance(other, Vector2):
            self.x *= other.x
            self.y *= other.y

    def mult(self, x=0, y=0):
        self.x *= x
        self.y *= y

    def div(self, other):
        if isinstance(other, Vector2):
            self.x /= other.x
            self.y /= other.y

    def div(self, x=0, y=0):
        self.x /= x
        self.y /= y

    def dot(self, other):
        if isinstance(other, Vector2):
            dot = self.x * other.x + self.y * other.y
            return dot

    def dot(self, x=0, y=0):
        dot = self.x * x + self.y * y
        return dot

    def dot(self, value):
        return self.dot(value, 0)

    def mag(self):
        mag = sqrt(self.x*self.x + self.y*self.y)
        return mag

    def magSq(self):
        magSq = self.x*self.x + self.y+self.y
        return magSq

    def normalize(self):
        len = self.mag()
        if (len != 0):
            self.mult(1/len)

    def setMag(self, val):
        self.normalize()
        self.mult(val)

    def dist(self, other):
        if isinstance(other, Vector2):
            v = other.copy()
            v.sub(self)
            dist = v.mag()
            return dist

    def limit(self, _max):
        mSq = self.magSq()
        if (mSq > _max*_max):
            self.div(sqrt(mSq))
            self.mult(_max)

    def heading(self):
        if self.x == 0:
            if self.y > 0:
                return 90
            elif self.y == 0:
                return 0
            else:
                return 270
        elif self.y == 0:
            if self.x >= 0:
                return 0
            else:
                return 180

    def print(self):
        print("("+str(self.x) + ", " + str(self.y)+")")


    
