counter = 0
mileage = 160648
def faulty_odometer(mileage):

for miles in range(mileage):
    if 5 in str(miles): 
        continue

        counter = counter + 1
return counter
print(faulty_odometer(mileage))