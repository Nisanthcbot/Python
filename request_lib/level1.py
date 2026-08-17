import requests
response  = requests.get("https://jsonplaceholder.typicode.com/users/3")

class EmployeePayroll:
    def __init__(self,emp_id,name,company,basic_salary=100000):
        self.emp_id = emp_id
        self.name= name
        self.company=company
        self.basic_salary = basic_salary

    def calculate_tax(self):
        tax = self.basic_salary *0.20
        return tax

    def generate_payslip(self):
        net_salary = self.basic_salary - self.calculate_tax()
        print(f"Employee :{self.name}, Company :{self.company}, Basic Salary : {self.basic_salary}, Tax Deduction :{self.calculate_tax()}, Net Pay : {net_salary}")
    
data = response.json()

emp=EmployeePayroll(data["id"],data["name"],data["company"]["name"])
emp.generate_payslip()

