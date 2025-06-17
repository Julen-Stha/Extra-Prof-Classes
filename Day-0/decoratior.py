class Student:
    school_name= " "
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade


    @classmethod
    def change_school_name(cls,school):
        cls.school_name = school

    def display_info(self):
        print(f"name = {self.name} grade = {self.grade} school name = {self.school_name}")

class Admin(Student):
    def __init__(self):
        self.students  = []
    
    def add(self,name,grade):
        self.students.append(Student(name,grade))

    def remove(self, name_to_remove, grade_to_remove):
        student_found = None
        for student in self.students:
            if student.name == name_to_remove and student.grade == grade_to_remove:
                student_found = student
                break # Found the student, no need to continue searching
        
        if student_found:
            self.students.remove(student_found)
            print(f"Removed student: {name_to_remove}")
        else:
            print(f"Student '{name_to_remove}' with grade '{grade_to_remove}' not found.")

    def display(self):
        for x in self.students:
            print(x.name)
        


student1 = Student("Julen", 10)
student2 = Student("gayson", 11)
student1.change_school_name("nagarjuna")
student1.display_info()
student2.change_school_name("columbus")
student2.display_info()
a= Admin()
a.add("aveg",10)
a.display()
a.remove("aveg",10)
a.display()



              

    
