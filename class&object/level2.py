"""
1)Create a class named QueueTicket.

2)Write the __init__ constructor to accept customer_name and service_type (e.g., "Consultation", "Billing").

3)Inside the constructor, assign those to self, but also add a third variable: self.status = "Waiting". (Do not put status in the __init__ parameters).

4)Write a method called show_status(self) that returns:
"Ticket for [customer_name] | Service: [service_type] | Status: [status]"

5)Write a second method called serve_customer(self). This method should change self.status to "Served" and return the string: "Now serving [customer_name]..."

6)Outside the class, create an object called ticket_one for a customer named "Rahul" who is there for "Billing".

7)Print the result of ticket_one.show_status().

8)Print the result of ticket_one.serve_customer().

9)Print the result of ticket_one.show_status() one last time to prove the status actually changed!

"""

class QueueTicket():

    def __init__(self,customer_name, service_type):

        self.customer_name = customer_name
        self.service_type = service_type
        self.status = "Waiting"

    def show_status(self):
        return f"Ticket for {self.customer_name} | Service: {self.service_type} | Status: {self.status}"


    def serve_customer(self):
        self.status = "Served"
        return f"Now serving {self.customer_name}..."


ticket_one = QueueTicket("Rahul","Billing")

print(ticket_one.show_status())
print(ticket_one.serve_customer())
print(ticket_one.show_status())
        