def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

print("Area of the triangle:", calculate_area(a, b, c))