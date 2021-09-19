#Keyword arguments
def increment(number, by):
    return number + by


print(increment(2, 1))

#args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))