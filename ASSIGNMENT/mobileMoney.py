class MobileMoney:

    """A class representing a Mobile Money account with data hiding."""

    def __init__(self, initial_balance=0):

        # Data Hiding: The double underscore makes '__balance' private

        self.__balance = initial_balance 



    def deposit(self, amount):

        """Securely add money to the balance."""

        if amount > 0:

            self.__balance += amount

            print(f"UGX {amount:,} deposited successfully.")

        else:

            print("Invalid deposit amount.")



    def withdraw(self, amount):

        """Securely deduct money after checking current funds."""

        if amount <= 0:

            print("Invalid withdrawal amount.")

        elif amount > self.__balance:

            print(f"Transaction Failed: Insufficient funds to withdraw UGX {amount:,}.")

        else:

            self.__balance -= amount

            print(f"UGX {amount:,} withdrawn successfully.")



    def check_balance(self):

        """Public method to safely view the hidden balance."""

        return self.__balance


print("=== Mobile Money System ===")


# 1. Initialize the account with a starter balance of UGX 500,000

my_account = MobileMoney(500000)

print(f"Starting Balance: UGX {my_account.check_balance():,}")

print("-" * 35)


# 2. Testing standard deposit

my_account.deposit(200000)  

print("-" * 35)


# 3. Testing  standard withdrawal

my_account.withdraw(150000) 

print("-" * 35)


# 4. Final verification showing balance after withdrawal

final_balance = my_account.check_balance()

print(f"Final Balance after withdrawal: UGX {final_balance:,}")

print("===========================")


# print(my_account.__balance) will bring an error because '__balance' is hidden.