class Car:

    def __init__(self, brand, model, price):

        self.brand = brand          # Public attribute

        self._model = model         # Protected attribute (single underscore)

        self.__price = price        # Private attribute (double underscore)



    def display_details(self):

        """Method to display all values appropriately from within the class"""

        print("--- Car Details ---")

        print(f"Brand (Public):    {self.brand}")

        print(f"Model (Protected): {self._model}")

        print(f"Price (Private):   {self.__price}")


# 1. Create an instance of the Car class

my_car = Car("Toyota", "Camry", 24000)



# 2. Display all values using the class's internal method

my_car.display_details()



print("\n--- Direct Access Demonstration ---")

# 3. Demonstrating how access rules apply outside the class:



# Accessing Public: Works perfectly

print(f"Direct access to Brand: {my_car.brand}")



# Accessing Protected

print(f"Direct access to Model: {my_car._model}")


# Accessing Private: This will raise an AttributeError if uncommented!
# print(f"Direct access to Price: {my_car.__price}") 

print("Direct access to __price fails outside the class because it is private.")