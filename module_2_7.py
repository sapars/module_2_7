# Самостоятельная работа по уроку "Рекурсия"

# Задача "Рекурсивное умножение цифр":
# апиши функцию get_multiplied_digits,
# которая принимает аргумент целое чиcло number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(number=1):
    if len(str(number)) == 1:
        return number
    return int(str(number)[0]) * get_multiplied_digits(int(str(number)[1:]))


print(get_multiplied_digits(14574574584500607))
