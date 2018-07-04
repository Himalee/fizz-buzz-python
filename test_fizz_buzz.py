import pytest

from fizz_buzz import *

class TestFizzBuzz():

    def test_convert_number_one(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(1) == 1

    def test_convert_number_two(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(2) == 2

    def test_convert_number_three(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(3) == "Fizz"

    def test_convert_number_four(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(4) == 4

    def test_convert_number_five(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(5) == "Buzz"

    def test_convert_number_six(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(6) == "Fizz"

    def test_convert_number_ten(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(10) == "Buzz"

    def test_convert_number_fifteen(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(15) == "Fizz Buzz"

    def test_convert_number_thirty(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.convert_number(30) == "Fizz Buzz"
