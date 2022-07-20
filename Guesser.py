from random import *

def is_valid(num, n):
    if 1<=num<=n:
        return True
    else:
        return False

def choose_bound():
    print("Выберите правую границу случайного числа:")
    return int(input())

num = choose_bound()
rand_number = randint(1, num)
print("Добро пожаловать в числовую угадайку!")
flag = True
count = 0
while flag:
    possible_number = int(input())
    if is_valid(possible_number, num):
        if possible_number<rand_number:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count += 1
        elif possible_number>rand_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count += 1
        else:
            print("Вы угадали, поздравляем!" + f" Число попыток: {count}")
            print("Хотите сыграть еще раз?")
            _flag = True
            while _flag:
                s = input()
                if s.lower() == "yes":
                    num = choose_bound()
                    rand_number = randint(1, num)
                    count = 0
                    _flag = False
                elif s.lower() == "no":
                    _flag = False
                    flag = False
                else:
                    print("Извините, я вас не понимаю")
    else:
        print(f"А может быть все-таки введем целое число от 1 до {num}?")
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
