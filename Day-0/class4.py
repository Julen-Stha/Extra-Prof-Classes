class Employee:
    emp_id = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.employee_id = Employee.emp_id
        Employee.generate_emp_id()

    def get_info(self):
        print(f"Full Name: {self.first_name} {self.last_name}")

    def get_email(self):
        print(f"Email: {self.first_name.lower()}.{self.last_name.lower()}@gmail.com")

    @classmethod
    def generate_emp_id(cls):
        cls.emp_id += 1


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, language):
        super().__init__(first_name, last_name, salary)
        self.language = language

    def get_info(self):
        print(f"Language: {self.language}")



print(f"Initial Employee.emp_id: {Employee.emp_id}")

a = Developer("Juleln", "shrestha", 8000000,"Python")
print(f"Assigned ID for 'a': {a.employee_id}")
print(f"Current Employee.emp_id after 'a' creation: {Employee.emp_id}")
