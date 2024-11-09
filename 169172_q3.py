class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to ${self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} (ID: {employee.employee_id}) to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: ${total_salary}")

    def display_all_employees(self):
        print(f"\nEmployees in {self.department_name} Department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")

def main():
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("Department Management System:\n")
        print("1. Add an employee")
        print("2. Display all employees")
        print("3. Update an employee's salary")
        print("4. Display total salary expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == '2':
            department.display_all_employees()

        elif choice == '3':
            emp_id = input("Enter the employee ID to update salary: ")
            new_salary = float(input("Enter the new salary: "))
            for employee in department.employees:
                if employee.employee_id == emp_id:
                    employee.update_salary(new_salary)
                    break
            else:
                print("Employee not found.")

        elif choice == '4':
            department.calculate_total_salary_expenditure()

        elif choice == '5':
            print("Exiting the department management system.")
            break

        else:
            print("Invalid choice. Please try again.")
main()