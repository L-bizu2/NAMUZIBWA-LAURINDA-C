class User:

    """A class representing a standard user profile."""

    def __init__(self, first_name, last_name, username, location, role="Student"):

        self.first_name = first_name

        self.last_name = last_name

        self.username = username

        self.location = location

        self.role = role



    def describe_user(self):

        print("--- USER ACCOUNT SUMMARY ---")

        print(f"Full Name: {self.first_name} {self.last_name}")

        print(f"Username:  @{self.username}")

        print(f"Location:  {self.location}")

        print(f"System Role: {self.role}")



    def greet_user(self):

        print(f"👋 Hello {self.first_name}! Welcome back to your workspace console dashboard.\n")

print("---User Profiles ---")

# 1. Instantiating several different users

user_one = User("Laurinda", "Namuzibwa", "laurynda_c", "Kampala, Uganda", "Administrator")

user_two = User("Moses", "Kato", "moses_k", "Entebbe, Uganda", "Software Engineer")

user_three = User("Alvin", "Mukasa", "alvin_99", "Jinja, Uganda")

# 2. Call profile descriptions and greetings for each user object instance
user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()