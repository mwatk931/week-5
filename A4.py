def calculate_average(temperatures):
    return round(sum(temperatures) / len(temperatures), 2)


def find_highest(temperatures):
    return max(temperatures)


def find_lowest(temperatures):
    return min(temperatures)


def count_hot_days(temperatures):
    return sum(1 for temperature in temperatures if temperature > 20)


temperature_input = input("Enter temperatures separated by commas: ")

temperatures = [float(value.strip()) for value in temperature_input.replace(" ", ",").split(",") if value.strip()]

print(f"Average temperature: {calculate_average(temperatures):g}")
print(f"Highest temperature: {find_highest(temperatures)}")
print(f"Lowest temperature: {find_lowest(temperatures)}")
print(f"Number of hot days: {count_hot_days(temperatures)}")