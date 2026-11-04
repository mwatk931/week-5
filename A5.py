def unique_sorted(numbers):
	return sorted(set(numbers), reverse=True)

input_numbers = input("Enter a list of numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_numbers.split(",")]
print("Unique numbers sorted in descending order:", unique_sorted(numbers))