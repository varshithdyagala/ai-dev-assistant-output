fib_sequence = [0, 1]

for i in range(2, 10):
    next_value = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_value)

for number in fib_sequence:
    print(number)