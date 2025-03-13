employees = []

def add_employee(emp_id, name, age, department):
    for employee in employees:
        if employee[0] == emp_id:
            print("Error: Employee ID already exists!")
            return
    if not name.isalpha():
        print("Error: Name must contain only alphabets!")
        return
    if not age.isdigit() or int(age) <= 0:
        print("Error: Age must be a positive integer!")
        return
    employees.append([emp_id, name, int(age), department])
    print("Employee added successfully!")

def remove_employee(emp_id):
    for employee in employees:
        if employee[0] == emp_id:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
    print("Error: Employee ID not found!")

def update_employee(emp_id, name=None, age=None, department=None):
    for employee in employees:
        if employee[0] == emp_id:
            if name and not name.isalpha():
                print("Error: Name must contain only alphabets!")
                return
            if age and (not age.isdigit() or int(age) <= 0):
                print("Error: Age must be a positive integer!")
                return
            if name:
                employee[1] = name
            if age:
                employee[2] = int(age)
            if department:
                employee[3] = department
            print("Employee updated successfully!")
            return
    print("Error: Employee ID not found!")

def search_employee(query):
    found = False
    for employee in employees:
        if employee[0] == query or employee[1].lower() == query.lower():
            print(f"ID: {employee[0]}, Name: {employee[1]}, Age: {employee[2]}, Department: {employee[3]}")
            found = True
    if not found:
        print("Error: Employee not found!")

def sort_employees(key_index):
    if key_index not in [1, 2, 3]:
        print("Error: Invalid sort key! Choose 'name', 'age', or 'department'.")
        return
    sorted_employees = sorted(employees, key=lambda x: x[key_index])
    print("Sorted Employees:")
    for employee in sorted_employees:
        print(f"ID: {employee[0]}, Name: {employee[1]}, Age: {employee[2]}, Department: {employee[3]}")

def employee_management_system():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            add_employee(emp_id, name, age, department)
        elif choice == "2":
            emp_id = input("Enter Employee ID to remove: ")
            remove_employee(emp_id)
        elif choice == "3":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter New Name (leave blank to skip): ") or None
            age = input("Enter New Age (leave blank to skip): ") or None
            department = input("Enter New Department (leave blank to skip): ") or None
            update_employee(emp_id, name, age, department)
        elif choice == "4":
            query = input("Enter Employee ID or Name to search: ")
            search_employee(query)
        elif choice == "5":
            print("Sort by: 1. Name, 2. Age, 3. Department")
            key_index = int(input("Enter your choice (1/2/3): "))
            sort_employees(key_index)
        elif choice == "6":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

employee_management_system()
