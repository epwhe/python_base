# -*- coding: utf-8 -*-

# Условный оператор (ветвление потока выполнения)

# if <услови>е:
#     <блок кода 1>

x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')

# операторы сравнения
# >
# <
# >=
# <=
# ==
# !=

# группировка условий
# or
# and
# not


# примеры
a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b < 10:
    print('успех')


# можно сравнивать - числа, строки, списки, вообще - переменные одного типа

if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

# что нельзя сравнивать - разные типы
if '6' > 5:
    print('успех')

if [5, 6] > 5:
    print('успех')

# но
if '6' != 5:
    print('успех')

# Блок иначе
# if <условие>:
#     <блок кода 1>
# else:
#     <блок кода 2>

x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
else:
    print('Больше нуля')
print('дотвидания!')


# множественный выбор (аналог CASE)

# if <условие>:
#     <блок кода 1>
# elif <условие>:
#     <блок кода 2>
# elif <условие>:
#     <блок кода 3>
# else:
#     <блок кода 4>

print('дратути!')
if x < 0:
    print('Меньше нуля')
elif x == 0:
    print('Равно нулю')
elif x == 1:
    print('Равно единице')
else:
    print('Больше нуля, но не равно единице')
print('дотвидания!')

# блок кода - может быть много операторов и даже вложенные
print('дратути!')
if x < 0:
    print('Меньше нуля')
    result = -1
elif x == 0:
    print('Равно нулю')
    result = 0
elif x == 1:
    print('Равно единице')
    result = 1
else:
    print('Больше нуля, но не равно единице')
    if x == 42:
        print('Вау!')
    result = 42
print('дотвидания!')

# Трехместное выражение - короткая запись для простого случая

# if x < 0:
#     result = 'Меньше нуля'
# else:
#     result = 'Больше нуля'
result = 'Меньше нуля' if x < 0 else 'Больше нуля'
