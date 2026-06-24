class ContactManager:

    """Manages a collection of system contacts with robust data validation."""



    def __init__(self):

        # Dictionary to store contact records using name as the key

        self.contacts = {}



    def _validate_phone(self, phone):

        """Helper method to ensure phone number contains only digits and hyphens."""

       

        clean_phone = phone[1:] if phone.startswith('+') else phone

        

        # Replace hyphens with empty space to check if remaining characters are entirely digits

        if not clean_phone.replace('-', '').isdigit():

            return False

        return True



    def _validate_email(self, email):

        """Helper method to ensure email contains both '@' and '.' characters."""



        # If no email is provided (blank string), we treat it as valid/optional

        if not email:

            return True

        if "@" in email and "." in email:

            return True

        return False



    def add_contact(self, name, phone, email=""):

        """Validates and appends a brand new entry to the directory list."""



        # Run Phone Validation Checks

        if not self._validate_phone(phone):

            print(f"❗️ Error adding '{name}': Invalid phone number format! Use only digits and hyphens (e.g., '+256-701').")

            return False

            

        #Run Email Validation Checks

        if not self._validate_email(email):

            print(f"❗️Error adding '{name}': Invalid email layout! Must contain both '@' and '.' signs.")

            return False



        #Saves contact if tests pass

        self.contacts[name] = {"phone": phone, "email": email}

        print(f"✅ Contact '{name}' added successfully.")

        return True



    def update_contact(self, name, phone, email=""):

        """Securely modifies data records for preexisting directory entries."""

        if name not in self.contacts:

            print(f"❗️ Error: '{name}' does not exist in your contacts directory.")

            return False



        # Validate updates before saving over old data records

        if not self._validate_phone(phone):

            print(f"❗️Error updating '{name}': Invalid phone number format!")

            return False



        if not self._validate_email(email):

            print(f"❗️Error updating '{name}': Invalid email format!")

            return False



        self.contacts[name] = {"phone": phone, "email": email}

        print(f"🔄 Contact '{name}' updated successfully.")

        return True



    def display_contacts(self):

       

        print("\n=== CURRENT CONTACT DIRECTORY ===")

        if not self.contacts:

            print("[Empty Directory]")

        for name, details in self.contacts.items():

            print(f"👤 Name: {name} | 📱 Phone: {details['phone']} | ✉️ Email: {details['email'] or 'N/A'}")

        print("=================================")





print("=== Starting Contact Manager Project ===")

manager = ContactManager()



#Testing valid contact insertion

manager.add_contact("Laurinda", "+256-701", "laurinda@example.com")



#Testing phone validation failure (contains illegal letters)

manager.add_contact("Invalid Phone User", "+256-701-KAMPALA", "test@test.com")



#Testing email validation failure (missing period)

manager.add_contact("Invalid Email User", "0700-111-222", "bademail@domain")



#Testing valid data update

manager.update_contact("Laurinda", "+256-777-888", "laurinda.new@example.com")



#Testing invalid data update 

manager.update_contact("Laurinda", "CRASH-NUMBER", "laurinda@example.com")



# Display the end results of the internal record state

manager.display_contacts()