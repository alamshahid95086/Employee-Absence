


from datetime import date

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.total_absence = 0
        self.exit_absence = 0
        self.taken_absence = 0
        self.leave_records = []

    def add_leave(self, start_leave_date, end_leave_date):
        leave_days = (end_leave_date - start_leave_date).days + 1
        self.total_absence += leave_days
        self.taken_absence += leave_days
        self.leave_records.append((start_leave_date, end_leave_date))
        print(f"Leave added for {self.name}: {leave_days} days from {start_leave_date} to {end_leave_date}")

    def display_info(self):
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Total Absence: {self.total_absence} days")
        print(f"Taken Absence: {self.taken_absence} days")
        print("Leave Records:")
        for start_date, end_date in self.leave_records:
            print(f"  From {start_date} to {end_date}")

class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, employee_id):
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(name, employee_id)
            print(f"Employee {name} added.")
        else:
            print(f"Employee ID {employee_id} already exists.")

    def add_leave_to_employee(self, employee_id, start_leave_date, end_leave_date):
        if employee_id in self.employees:
            self.employees[employee_id].add_leave(start_leave_date, end_leave_date)
        else:
            print(f"Employee ID {employee_id} not found.")

    def display_all_employees(self):
        for employee in self.employees.values():
            employee.display_info()

def main():
    company = Company()
    
    while True:
        print("\n1. Add Employee")
        print("2. Add Leave to Employee")
        print("3. Display All Employees")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            company.add_employee(name, employee_id)
        
        elif choice == '2':
            employee_id = input("Enter employee ID: ")
            start_date_input = input("Enter start leave date (YYYY-MM-DD): ")
            end_date_input = input("Enter end leave date (YYYY-MM-DD): ")
            
            start_leave_date = date.fromisoformat(start_date_input)
            end_leave_date = date.fromisoformat(end_date_input)
            
            company.add_leave_to_employee(employee_id, start_leave_date, end_leave_date)
        
        elif choice == '3':
            company.display_all_employees()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



