class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print(f"No grades available for {self.name}.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
            print(f"Assigned grade {grade} for {assignment_name} to {student.name}.")
        else:
            print("Student not found.")

    def display_all_students_grades(self):
        print(f"\nGrades for all students in {self.course_name}:")
        if self.students:
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled.")

def main():
    instructor = Instructor("Prof. Atwoli", "Introduction to API")

    while True:
        print("Course Management System\n")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and their grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == '2':
            student_id = input("Enter the student's ID: ")
            assignment_name = input("Enter the assignment name: ")
            grade = input("Enter the grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == '3':
            instructor.display_all_students_grades()

        elif choice == '4':
            print("Exiting the course management system.")
            break

        else:
            print("Invalid choice. Please try again.")
main()