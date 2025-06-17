class Square:
    def __init__(self,length,color):
        self.length = length
        self.color = color
    def perimeter(self):
        print(f"Perimeter is {4*self.length}")

    def area(self):
        print(f"Area is {self.length*self.length}")



sq1 = Square(5,"blue")
sq1.perimeter()
sq1.area()