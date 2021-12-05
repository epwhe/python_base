from random import randrange

bulls_cows = {}
secret_number = None


def make_namber():
    global secret_number
    secret_number = randrange(1000, 9999)
    return secret_number


# print(make_namber())

def check_number(number):
    _hidden_numbers = secret_number
    result = {'bulls': 0, 'cows': 0}
    chk_numbers = []

    for char in map(int, number):
        chk_numbers.append(char)

    for pos, hidden_number in enumerate(_hidden_numbers):
        for chk_pos, number in enumerate(chk_numbers):
            if hidden_number == number:
                if pos == chk_pos:
                    result['bulls'] += 1
                    continue
                else:
                    result['cows'] += 1

    return result


if __name__ == '__main__':
    print(make_namber())
    input_number = 1241
    print(input_number)
    print(check_number(input_number))
    # print(chek_namber(secret_number=secret_number, input_number=input_number))
