def fibonacci(value):

    if value == 1:
        return 1
    elif value == 2:
        return 1
    else:
        a = 1
        b = 1
        i = 0
        while( i < value - 2):

            a, b = b, a + b
            i+=1

        return b

# Example usage:
example1 = 3

print(f" {example1}: {fibonacci(example1 + 1)}")

example1 = 5

print(f" {example1}: {fibonacci(example1 + 1)}")
