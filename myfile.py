import math

class Calculus_Calculator:
    def logarithm(x, base=10):
        return math.log(x, base)

    def power(x, y):
        return math.pow(x, y)

    def fact(x):
        return math.factorial(x)


print("Logarithm: " + str(Calculus_Calculator.logarithm(1000)))
print("Power: " + Calculus_Calculator.power(5, 2))  
print("Factorial: " + str(Calculus_Calculator.fact(7)))
