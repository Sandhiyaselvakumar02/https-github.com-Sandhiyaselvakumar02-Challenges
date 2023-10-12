class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


def sort_students(student_list):
    # sort the list of the students in descending order of CGPA
    sorted_students = sorted(student_list,
                             key=lambda student: student.cgpa,
                             reverse=True)
    return sorted_students


# Example usage:
students = [
    Student("Sandhiya", "A123", 7.8),
    Student("Dhanalakshmi", "A124", 8.9),
    Student("Girija", "A125", 9.1),
    Student("Gomathi", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of the students
for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                       student.roll_number,
                                                       student.cgpa))

  

