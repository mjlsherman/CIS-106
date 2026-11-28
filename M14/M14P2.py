class Student:
    def __init__(self, first_name, last_name, district, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district = district
        self.credits = credits

    def calculate_tuition(self):
        if self.district == "I":
            return self.credits * 250
        else:
            return self.credits * 500


first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
district = input("Enter district code (I or O): ").upper()
credits = int(input("Enter enrolled credits: "))

student = Student(first_name, last_name, district, credits)

print("Student:", student.first_name, student.last_name)
print("District code:", student.district)
print("Enrolled credits:", student.credits)
print(f"Tuition owed: ${student.calculate_tuition():,.2f}")
