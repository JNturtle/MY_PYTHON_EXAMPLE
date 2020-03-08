"""@proprety
blog: https://jnturtle.blogspot.com/2020/03/python-property.html#more
"""

if 1:
    class C(object):
        def __init__(self):
            self._x = None
        def getx(self):
            print("得了")
            return self._x 
        def setx(self, value):
            print("設了")
            self._x = value
        def delx(self):
            print("刪了")
            del self._x
        x = property(getx, setx, delx, "docstring")

    a = C()
    a.x # a.getx()
    a.x = 1 # a.setx()
    del a.x # a.delx()

if 0:
    class C(object):
        def __init__(self):
            self._x = None

        @property
        def x(self):
            print("得了")
            return self._x 

        @x.setter
        def x(self, value):
            print("設了")
            self._x = value 

        @x.deleter
        def x(self):
            print("刪了")
            del self._x

    a = C()
    a.x # call getter
    a.x = 1 # call setter 
    del a.x # call deleter


if 0:
    class Rectangle():
        def __init__(self, width, height):
            self.width = width
            self.height = height
        @property
        def area(self):
            return self.width * self.height

        def getArea(self):
            return self._width * self._height

    rect = Rectangle(5, 4)
    print(rect.area)
    print(rect.getArea())

if 0:
    class land():
        def __init__(self, width, height, pricePerPing):
            self._width = width
            self._height = height
            self._pricePerPing = pricePerPing

        @property
        def area(self):
            return self._width * self._height

        @property
        def price(self):
            return  self.area * self._pricePerPing

        def getArea(self):
            return self._width * self._height

        def getPrice(self):
            return  self.getArea() * self._pricePerPing

    myland = land(5, 4, 3)
    print(myland.area)    
    print(myland.price)
    print(myland.getArea())
    print(myland.getPrice())


if 0:
    def f1(f2):
        return 1

    @f1
    def f2(x):
        return 2
    print(f2) # 1
    f2(0) # ERROR


if 0:
    def addition(f):
        answer = 0
        for num in f():
            answer += num
        return answer

    @addition
    def threePlusFive():
        return [3, 5]

    @addition
    def threePlusFivePlusEight():
        return [3, 5, 8]

    @addition
    def threePlusFivePlusEight2():
        return [threePlusFive, 8]

    print(threePlusFive)
    print(threePlusFivePlusEight)
    print(threePlusFivePlusEight2)
