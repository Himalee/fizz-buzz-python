class FizzBuzz():
    def convert_number(self, number):
        if number % 15 == 0:
            return "Fizz Buzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        else:
            return number
