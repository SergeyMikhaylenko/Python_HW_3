# 3.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

Empty_line = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    Empty_line = str(n%2) + Empty_line
    n //=2
print(Empty_line)


