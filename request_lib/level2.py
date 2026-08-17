import requests

response = requests.get("https://jsonplaceholder.typicode.com/ /5")

class Tenant:

    def __init__(self,tenant_id,name,city,monthly_rent=12000,deposit_paid = True):

        self.tenant_id = tenant_id
        self.name = name
        self.city = city
        self.monthly_rent=monthly_rent
        self.deposit_paid = deposit_paid

    def calculate_late_fee(self,day_late=12):
        if day_late >5:
            late_fee = (day_late-5)*100
            return late_fee

    def generate_rent_receipt(self):

        print(f"Tenant Name :{self.name}, City : {self.city}, Monthly Rent : {self.monthly_rent}, Late Fee {self.calculate_late_fee()}")

data = response.json()

ten = Tenant(data["id"],data["name"],data["address"]["city"])
ten.generate_rent_receipt()
