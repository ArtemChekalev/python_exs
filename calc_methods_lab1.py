from math import *


print("Введите границы отрезка")
a, b = int(input()), int(input())
if a>b:
    a, b = b, a
segment = [a, b]
accuracy = 0
while accuracy == 0:
    accuracy = int(input("Введите точность (степень в выражении 10**x): "))
    if accuracy < 0:
        eps = 10 ** (accuracy)
    elif accuracy > 0:
        eps = 10 ** (-accuracy)
#величина невязки - величина ошибки приближенного равенства


def f(x):
    return 2**(-x) + 0.5 * x**2 - 10


def df(x):
    return (-log(2) + x*2**x)/(2**x)


def ddf(x):
    return (log(2)**2 +2**x)/2**x


def separation():
    n = 1000
    h, counter, a, segments = (segment[1] - segment[0]) / n, 0, segment[0], []
    b = a + h
    y1 = f(a)
    while b<=segment[1]:
        y2 = f(b)
        if y1*y2<=0:
            counter+=1
            segments.append([a, b])
        a = b
        b = a + h
        y1 = y2
    print('\n'f"Отрезки перемены знака:")
    for seg in segments:
        print(seg)
    print(f"Количество корней: {counter}")
    return segments


def bisection(segments):
    a, b = segments[0], segments[1]
    m = 0
    while b - a > 2 * eps:
        m += 1
        c = (b+a) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    X = (a + b)/2
    delta = (b - a) / 2
    print(f"Число шагов: {m}")
    print(f"Приближенное решение: {X}, длина последнего отрезка: {delta}")
    print(f"Абсолютная величина невязки: {abs(f(X) - 0)}")
    print("----------------------------------------------")


def newton(segments):
    a, b= segments[0], segments[1]
    if f(a)*ddf(a)>0:
        x = a
    else:
        x = b
    newX = x - f(x)/df(x)
    print(f"Начальные приближения к корню: {x, newX}")
    m = 0
    while abs(x - newX) >= eps:
        x, newX, m = newX, newX - f(newX)/df(newX), m + 1
    print(f"Число шагов: {m}")
    print(f"Приближенное решение: {newX}. \n|xm - xm-1| = {abs(newX-x)}")
    print(f"Абсолютная величина невязки: {abs(f(newX) - 0)}")
    print("----------------------------------------------")


def modified_newton(segments):
    a, b = segments[0], segments[1]
    if f(a) * ddf(a) > 0:
        x0 = a
        x = a
    else:
        x0 = b
        x = b
    newX = x - f(x) / df(x0)
    print(f"Начальные приближения к корню: {x0, newX}")
    m = 0
    while abs(x - newX) >= eps:
        x, newX, m = newX, newX - f(newX) / df(x0), m + 1
    print(f"Число шагов: {m}")
    print(f"Приближенное решение: {newX}. \n|xm - xm-1| = {abs(newX - x)}")
    print(f"Абсолютная величина невязки: {abs(f(newX) - 0)}")
    print("----------------------------------------------")


def secant(segments):
    a, b = segments[0], segments[1]
    x0 = a
    x1 = b
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    m = 0
    print(f"Начальные приближения к корню: {x0, x1, x2}")
    while abs(x1 - x0) >= eps:
        x0, x1, x2, m = x1, x2, x2 - (f(x2) * (x2 - x1)) / (f(x2) - f(x1)), m + 1
    print(f"Число шагов: {m}")
    print(f"Приближенное решение: {x1}. \n|xm - xm-1| = {abs(x1 - x0)}")
    print(f"Абсолютная величина невязки: {abs(f(x1) - 0)}")
    print("----------------------------------------------")


print("ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ"+'\n'+'Параметры задачи:'+'\n'+f'[A, B] = [{segment[0], segment[1]}]'+'\n'
    'f(x) = 2**(-x) + 0.5 * x**2 - 10'+'\n'+f'eps. = {eps}')


segments = separation()

for seg in segments:
    print('\n'"------Метод бисекций:")
    bisection(seg)
    print('\n'"------Метод Ньютона:")
    newton(seg)
    print('\n'"------Модифицированный метод Ньютона")
    modified_newton(seg)
    print('\n'"------Метод секущих")
    secant(seg)

