def multiply(a, b):
    # This is correct for the first run
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
