'''
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a \texttt{ operator } ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число -− результат вычисления.

Sample Input 1:

45 plus 8
Sample Output 1:

53
Sample Input 2:

12 minus 42
Sample Output 2:

-30
Sample Input 3:

451 multiply 2
Sample Output 3:

902
Sample Input 4:

13 divide 3
Sample Output 4:

4
'''


def simple_math_interpreter(string):
    import operator
    operator_value = {'plus': operator.add, 'minus': operator.sub, 'multiply': operator.mul,
                      'divide': operator.floordiv}
    val1, operator, val2 = string.split()
    return operator_value[operator](int(val1), int(val2))


print(simple_math_interpreter(input()))
