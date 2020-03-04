from sample import fizzbuzz

def test_return_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(3) == "Fizz"