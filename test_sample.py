from sample import fizzbuzz

def test_divisible_by_both():
    assert fizzbuzz(15) == "FizzBuzz"
def test_divisible_by_five():
    assert fizzbuzz(5) == "Buzz"
def test_divisible_by_three():
    assert fizzbuzz(3) == "Fizz"
def test_if_not_divisible_by_any():
    assert fizzbuzz(8) == 8