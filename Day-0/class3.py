class Shape:
    def __init__(self,color,isfilled):
        self.color = color
        self.isfilled = isfilled
    
    def describe(self):
        print(f"The color is {self.color} and {'is filled' if self.isfilled else 'not filled'}")

class square(Shape):
    def __init__(self, color, isfilled,lenght):
        super().__init__(color, isfilled)
        self.length = lenght

    def describe(self):
        super().describe()
        print(f"area is {self.length*self.length}")

class rectangle(Shape):
    def __init__(self, color, isfilled,lenght,breath):
        super().__init__(color, isfilled)
        self.length = lenght
        self.breath = breath

    def describe(self):
        super().describe()
        print(f"area is {self.length*self.breath}")

x= Shape("black",True)
x.describe()
y = square("red",True,5)
y.describe()
z = rectangle("blue",False,5,6)
z.describe()

