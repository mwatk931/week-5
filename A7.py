def max_difference(list1, list2):
    largest = abs(list1[0] - list2[0])

    for number1 in list1:
        for number2 in list2:
            difference = abs(number1 - number2)
            if difference > largest:
                largest = difference

    return largest
