def fizzbuzz(num):
    if num == 0:
        return num
    elif num % 5 == 0 and num %3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num