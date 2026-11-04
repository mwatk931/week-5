def calculate_fuel_cost(distance: float, mpg: float, price: float) -> float:
    gallons_needed = distance / mpg
    litres_needed = gallons_needed * 4.546  
    fuel_cost = litres_needed * price
    return fuel_cost

distance = float(input("Enter journey distance in miles: "))
mpg = float(input("Enter car fuel efficiency in MPG: "))
price = float(input("Enter petrol price per litre: "))

fuel_cost = calculate_fuel_cost(distance, mpg, price)
print("Fuel cost for the journey: £", fuel_cost)