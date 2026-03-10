def Add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    print(f"replaced: {numbers}")
    numbers = numbers.split(",")
    sumed = 0
    for number in numbers:
        if number is None:
            raise ValueError()
        number = int(number)
        sumed += number

    return sumed

Add("1,2")