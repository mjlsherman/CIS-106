class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, rate):
        return self.salary * rate


name = input("Enter employee name: ")
salary = float(input("Enter annual salary: "))

employee = Employee(name, salary)

rate = float(input("Enter bonus rate as a percentage: "))
bonus = employee.calculate_bonus(rate / 100)

print("Employee:", employee.name)
print(f"Annual salary: ${employee.salary:,.2f}")
print(f"Employee bonus: ${bonus:,.2f}")
