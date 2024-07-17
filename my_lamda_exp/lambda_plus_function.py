# Напиши функцию apply_operations_list, которая принимает два числа и список функций. Эта функция должна применить каждую функцию из списка к переданным числам и вернуть список результатов.

divide = lambda x, y: f'division {x / y}' if y != 0 else "Zero division error"
multiply = lambda x, y: f'multiplication {x * y}'
subtract = lambda x, y: f'subtraction {x - y}'
add = lambda x, y: f'addition {x + y}'
operations_list = [divide, multiply, subtract, add]


def apply_operations_list(x: float, y: float, operations:list) -> list:
    def apply_operation(x, y, operation):
        return operation(x, y)
    result = []
    for operation in operations:
        result.append(apply_operation(x, y, operation))
    return result

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(apply_operations_list(first_number, second_number, operations_list))
