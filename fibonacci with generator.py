fibonacci_numbers = list()
def fibonacci():
    
    a = 1
    b = 1
    yield a
    yield b

    while True:

        a,b = b,a+b

        yield b

for number in fibonacci():
    if number >100000:
        break
    else:
        fibonacci_numbers.append(number)
print(fibonacci_numbers)