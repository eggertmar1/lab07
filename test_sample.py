from sample import fizzbuzz

def test_divisible_by_both():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(-15) == "FizzBuzz"
def test_divisible_by_five():
    assert fizzbuzz(-5) == "Buzz"
    assert fizzbuzz(5) == "Buzz"
def test_divisible_by_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(-33) == "Fizz"
    assert fizzbuzz(-3) == "Fizz"
    assert fizzbuzz(-6) == "Fizz"
def test_if_not_divisible_by_any():
    assert fizzbuzz(8) == 8
    assert fizzbuzz(-8) == -8
    assert fizzbuzz(-2) == -2
    assert fizzbuzz(1) == 1
    assert fizzbuzz(-1) == -1

