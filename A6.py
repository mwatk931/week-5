def contains_duplicate(numbers):
    return len(numbers) != len(set(numbers))

input_numbers = input("Enter a list of numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_numbers.split(",")]
print(contains_duplicate(numbers))