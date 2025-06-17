class Pet:
    def __init__(self,name,age,medical_history={}):
        self.name= name
        self.age = age
        self.__medical_history = medical_history
    
    def speak(self):
        print("speak")

    def get_info(self):
        return self.name,self.age
    
    def add_medical_record(self,record):
         data = input(f"Enter data: {record}: ")
         self.__medical_history[record] = data

    def view_medical_history(self):
        return self.__medical_history
    

class Dog(Pet):
    def speak(slef):
        print("woof")

class Cat(Pet):
    def speak(self):
        print("meow")

class parrot(Pet):
    def speak(self):
        print("squawk")

def interact_with_pet(pet):
    pet.speak()


cat1 = Cat("Julen", 15)
cat1.add_medical_record("17-April-2025")
cat1.add_medical_record("25-April-2025")
print(cat1.view_medical_history())
name, age = cat1.get_info()
print(name, age)

interact_with_pet(cat1)



