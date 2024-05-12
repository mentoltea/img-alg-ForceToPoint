import math

GRAVITY_CONST = 1

with open("weigthmeasure.txt") as f:
    WEIGTHALG = f.read()
f.close()

class Color:
    r: int
    g: int
    b: int
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
        
    def __init__(self, color: tuple[int, int, int]):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
    
    def mass(self) -> int:
        r, g, b = self.r, self.g, self.b
        result: float
        result = eval(WEIGTHALG)
        return result
        
         
class Point:
    x: int
    y: int
class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distSquare(self, point: Point) -> int:
        return (self.x-point.x)*(self.x-point.x) + (self.y-point.y)*(self.y-point.y)

class Pixel:
    color: Color
    point: Point
class Pixel:
    color: Color
    point: Point
    def __init__(self, color, point):
        self.color = color
        self.point = point
    
    def forceTo(self, pixel: Pixel) -> float:
        mass1 = self.color.mass()
        mass2 = pixel.color.mass()
        ds = self.point.distSquare(pixel.point)
        if ds==0:
            return math.inf
        return GRAVITY_CONST*mass1*mass2/ds
