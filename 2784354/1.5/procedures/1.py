def digits(number):
    while number:
        print(number%10)
        number //=10