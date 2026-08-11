"""
Create a class named EmployeeProfile.

Write the __init__ constructor to accept employee_name and base_salary.

Inside the constructor, assign those to self, and add a third variable: self.bonus = 0 (this sets the default bonus to zero).

Write a method called add_bonus(self, amount). This method should take in an amount as a parameter and add it to self.bonus.

Write another method called calculate_payout(self). This method should add the base_salary and the bonus together, and return a string: "Total Payout for [employee_name]: ₹[total_amount]".

Outside the class, create an object for an employee named "Karthik" with a base salary of 45000.

Call the add_bonus() method and pass in 5000.

Print the result of calculate_payout()


"""


class EmployeeProfile():

    def __init__(self,employee_name,basic_salary ):
        self.employee_name = employee_name
        self.basic_salary = basic_salary
        self.bonus = 0


    def add_bonus(self,amount):
        self.bonus = self.bonus + amount
        return self.bonus

    def calculate_payout(self):
        total_amount = self.basic_salary + self.bonus
        return f"Total Payout for {self.employee_name}: ₹{total_amount}"


emp = EmployeeProfile("Karthik",45000)

print(emp.add_bonus(5000))
print(emp.calculate_payout())

