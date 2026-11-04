def calculate_percentage(number: int) -> float:
    return number * 23 / 100


if __name__ == "__main__":
    integer = int(input("Enter projected sales: "))
    print("Expected Profit:", calculate_percentage(integer))