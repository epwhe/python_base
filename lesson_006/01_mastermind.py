# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import make_number, check_number
from termcolor import cprint
from random import randint as rnd


result = {'bulls': 0, 'cows': 0}
count = 0


def bot_player(bulls, cows):

    number = []

    if bulls == 0:
        for i in range(4):
            if i == 0:
                number.append(rnd(1, 9))
            else:
                number.append(rnd(0, 9))
    return number


while True:

    if count == 0:
        is_bot = True if input('Доверите игру БОТУ? (y/n)') in ('Y', 'y', 'д', 'Д') else False
        cprint('Число загадано', 'green')
        cprint(make_number(), 'green')

    if is_bot:
        print('Укажите число: ')
        chk_number = bot_player(result['bulls'], result['cows'])
    else:
        chk_number = input('Укажите число: ')

    print(chk_number)

    result = check_number(chk_number)
    cprint('быки - ' + str(result['bulls']) + ' коровы - ' + str(result['cows']), 'blue')
    count += 1

    if result['bulls'] == 4:
        cprint('!!! ПОБЕДА !!!', 'red')
        cprint('Кол-во попыток: ' + str(count), 'red')
        result_ask = input('Хотите еще партию? (y/n)')

        if result_ask in ('Y', 'y', 'д', 'Д'):
            count = 0
            continue
        else:
            break
