# Program to calculate the area of a rectangle

print("=== Rectangle Area Calculator ===")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


area = length * width


print(f"\nResults:")
print(f"-> Length: {length}")
print(f"-> Width:  {width}")
print(f"-> The calculated Area is: {area:.2f}")