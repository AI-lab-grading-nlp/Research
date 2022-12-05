def calculate(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return x / y
    else:
        return 'Invalid operation'


