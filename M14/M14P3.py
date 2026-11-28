class Student:
    def __init__(self, first_name, last_name, district, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district = district
        self.credits = credits

    def calculate_tuition(self):
        rates = {
            "I": 250,
            "O": 500,
            "X": 800,
            "G": 250
        }

        return self.credits * rates[self.district]

    def display_student(self):
        print("Student:", self.first_name, self.last_name)
        print("District code:", self.district)
        print("Enrolled credits:", self.credits)
        print(f"Tuition owed: ${self.calculate_tuition():,.2f}")
        print()


student1 = Student("John", "Smith", "I", 12)
student2 = Student("Jane", "Brown", "O", 15)
student3 = Student("David", "Lee", "X", 12)
student4 = Student("Sarah", "Jones", "G", 9)

student1.display_student()
student2.display_student()
student3.display_student()
student4.display_student()
