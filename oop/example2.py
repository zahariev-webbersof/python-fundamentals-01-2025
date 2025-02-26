def introduce(name, age, town):
    return f'My name is {name} and im {age} years old from {town}'


name = 'Gosho'
age = 15
town = 'Plovdiv'
introduce(name, age, town)

def calculate_result(operation, num1, num2):
    if operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return int(num1 / num2)
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2


operation = input()
first_number = int(input())
second_number = int(input())
result = calculate_result(operation, first_number, second_number)
print(result)