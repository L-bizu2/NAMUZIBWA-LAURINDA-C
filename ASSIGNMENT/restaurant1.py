class Restaurant:

    """A simple class to model a restaurant."""



    def __init__(self, restaurant_name, cuisine_type):

        """Initialize name and cuisine type attributes."""

        self.restaurant_name = restaurant_name

        self.cuisine_type = cuisine_type



    def describe_restaurant(self):

        """Print a summary description of the restaurant."""

        print(f"Restaurant Name: {self.restaurant_name}")

        print(f"Cuisine Type: {self.cuisine_type}")



    def open_restaurant(self):

        """Print a message indicating that the restaurant is now open."""

        print(f"✨ {self.restaurant_name} is now OPEN! ✨")







print("--- Exercise 9-1: Single Restaurant ---")





restaurant = Restaurant("Cafe Javas", "Continental and Ugandan Local")





print(f"Accessing Attribute 1 directly: {restaurant.restaurant_name}")

print(f"Accessing Attribute 2 directly: {restaurant.cuisine_type}")

print("-" * 30)





restaurant.describe_restaurant()

restaurant.open_restaurant()

print("\n")