#__private
#_ protected
class Animal:
    def __init__(self,name):
        self._name = name
        
    def method_one():
        pass

    def sound(self):
        print("animal sound")


class Cat(Animal):
    def method_two():
        pass

    def sound(self):
        print("meow")

animal1=Animal("animal")
animal1.sound()
cat1 = Cat("tom")
cat1.sound()


