from random import *

def generate_password(password_length, chars):
    passw = ''
    for _ in range(int(password_length)):
        passw += choice(chars)
    return passw

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ''

number_of_passwords = input("Укажите число паролей для генерации" + '\n')
password_length = input("Укажите длину пароля" + '\n')
flag_digits = input("Включать ли цифры 0123456789?"+ " yes/no" + '\n' )
flag_Upper = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?" + " yes/no" + '\n')
flag_lower = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?" + " yes/no" + '\n')
flag_symbols = input("Включать ли символы !#$%&*+-=?@^_?" + " yes/no" + '\n')
flag_differ = input("Исключать ли неоднозначные символы il1Lo0O?" + " yes/no" + '\n')
if flag_digits == 'yes':
    chars += digits
if flag_Upper == 'yes':
    chars += uppercase_letters
if flag_lower == 'yes':
    chars += lowercase_letters
if flag_symbols == 'yes':
    chars += punctuation
if flag_differ == 'yes':
    for i in "il1Lo0O":
        chars = chars.replace(i, "")
for i in range(1, int(number_of_passwords)+1):
    print(f"Пароль №{str(i)}: "+generate_password(password_length, chars))