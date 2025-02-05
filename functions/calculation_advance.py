def calculate_result(operation, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtract': num1 - num2
    }.get(operation, 'Invalid operator')


operator = input()
first_number = int(input())
second_number = int(input())
result = calculate_result(operator, first_number, second_number)
print(result)