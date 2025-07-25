# Create a class structure for Employee Management System: 
# 1. Abstract Class: Employee 
# ○ Abstract method: calculate_salary() 
# 2. Child Classes: FullTimeEmployee, PartTimeEmployee 
# ○ Full-time: monthly salary 
# ○ Part-time: hourly wage × hours worked 
# 3. Add common attribute: name, id (in base) 
# 4. Add method show_details() to print employee info 
#  Use: 
# ● Inheritance 
# ● Abstraction 
# ● Encapsulation (use private variables) 
# ● Polymorphism (override calculate_salary()) 

from abc import ABC, abstractmethod  # For abstraction

# 🔹 Abstract Base Class
class Employee(ABC):
    def __init__(self, name, emp_id):
        self.__name = name        # Private variable
        self.__id = emp_id        # Private variable

    def show_details(self):
        print(f"Name: {self.__name}, ID: {self.__id}")

    @abstractmethod
    def calculate_salary(self):
        pass  # Must be overridden by child

# 🔸 Full-time Employee (inherits Employee)
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.__monthly_salary = monthly_salary  # Encapsulated

    def calculate_salary(self):  # Polymorphism (method override)
        return self.__monthly_salary

# 🔸 Part-time Employee (inherits Employee)
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_wage, hours_worked):
        super().__init__(name, emp_id)
        self.__hourly_wage = hourly_wage
        self.__hours_worked = hours_worked

    def calculate_salary(self):  # Polymorphism (method override)
        return self.__hourly_wage * self.__hours_worked

# Create objects
f = FullTimeEmployee("Aditya", 101, 40000)
p = PartTimeEmployee("Ravi", 202, 500, 40)

# Show details & salary
print("== Full-Time Employee ==")
f.show_details()
print("Salary:", f.calculate_salary())

print("\n== Part-Time Employee ==")
p.show_details()
print("Salary:", p.calculate_salary())
