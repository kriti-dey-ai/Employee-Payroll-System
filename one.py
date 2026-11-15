class Employee:
    def __init__(self, emp_id, name, basic, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.overtime_hours = overtime_hours
    def calculate_gross(self):
        overtime = self.overtime_hours * 200
        gross = self.basic + overtime
        return gross
    def calculate_net(self):
        gross = self.calculate_gross()
        pf = 0.12 * self.basic
        if gross > 50000:
            tax = 0.10 * gross
        else:
            tax = 0
        net = gross - pf - tax
        return net
class Manager(Employee):
    def calculate_gross(self):
        overtime = self.overtime_hours * 200
        bonus = 0.10 * self.basic
        gross = self.basic + overtime + bonus
        return gross
def print_payslip(emp):
    overtime = emp.overtime_hours * 200
    gross = emp.calculate_gross()
    pf = 0.12 * emp.basic
    
    if gross > 50000:
        tax = 0.10 * gross
    else:
        tax = 0
    net = emp.calculate_net()
    # Format the payslip text
    if isinstance(emp, Manager):
        bonus = 0.10 * emp.basic
        slip = f"Manager: {emp.emp_id}, {emp.name}\nOvertime: {overtime} | Bonus: {bonus} | Gross: {gross}\nPF: {pf} | Tax: {tax}\nNet Salary: {net}\n--------------------\n"
    else:
        slip = f"Employee: {emp.emp_id}, {emp.name}\nOvertime: {overtime} | Gross: {gross}\nPF: {pf} | Tax: {tax}\nNet Salary: {net}\n--------------------\n"
    print(slip)
    # Save the payslip to payroll.txt
    file = open("payroll.txt", "a")
    file.write(slip)
    file.close()
# Main program loop
while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "3":
        print("Exiting program. All payslips are saved in payroll.txt.")
        break 
    if choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue    
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ") 
    # Input validation for Basic Salary
    while True:
        try:
            basic = float(input("Enter Basic Salary: "))
            if basic <= 0:
                print("Invalid basic salary. Enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid basic salary. Enter a positive number.")       
    # Input validation for Overtime Hours
    while True:
        try:
            overtime_hours = float(input("Enter Overtime Hours: "))
            if overtime_hours < 0:
                print("Invalid overtime hours. Enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Invalid overtime hours. Enter a non-negative number.")           
    # Create object based on choice
    if choice == "1":
        emp = Employee(emp_id, name, basic, overtime_hours)
    else:
        emp = Manager(emp_id, name, basic, overtime_hours) 
    print_payslip(emp)