"""
Your Task:

1)Create a class called PropertyListing.

2)Write an __init__ constructor that takes three parameters: self, property_name, and rent_price. (Inside the constructor, assign them to self.property_name and self.rent_price).

3)Add a method inside the class called display_listing(self) that prints out a formatted f-string: "Property: [Name] | Rent: ₹[Price]".

4)Outside the class, create an object named listing_one using your new class, passing in "Skyline Towers" and 15000 as the data.

5)Call the display_listing() method on listing_one.


"""


class PropertyListing():

    def __init__(self,property_name,rent_price):
        self.property_name = property_name
        self.rent_price = rent_price

    def display_listing(self):
        return f"Property: {self.property_name} | Rent: ₹{self.rent_price}"



listing_one = PropertyListing("Skyline Towers",15000)

print(listing_one.display_listing())



