# ==========================================
# GLOBAL VARIABLE
# ==========================================
# This variable is created outside of any function.
# It can be read by ANY function inside this entire script.
country = "Uganda"

def show_global_variable():
    print(f"[Inside show_global_variable] I can see the global variable 'country': {country}")

def local_variable_demo():
    # ==========================================
    # LOCAL VARIABLE
    # ==========================================
    # This variable is created INSIDE a function.
    # It belongs ONLY to this function. Nothing outside can see it.
    city = "Kampala"
    print(f"[Inside local_variable_demo] I can see my local variable 'city': {city}")
    print(f"[Inside local_variable_demo] I can also still see the global 'country': {country}")


print("--- Starting Program ---")

# 1. Call the first function
show_global_variable()
print("------------------------")

# 2. Call the second function
local_variable_demo()
print("------------------------")

# 3. Trying to access the local variable from the global scope (Outside)
print(f"[Outside] Checking the global variable 'country': {country}")

try:
    print(f"[Outside] Trying to check the local variable 'city': {city}")
except NameError as error:
    print(f"[ERROR OUTSIDE] Cannot print 'city'! Error details: {error}")

print("--- Program Ended ---")