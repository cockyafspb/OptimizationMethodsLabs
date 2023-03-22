# шаг сетки для дифференцирования (чем меньше, тем точнее)
H = 0.0000001

# разбиение для интегрирования (чем больше, тем точнее)
# если нужно посчитать шаг интегрирования, делаем так: (b - a) / N
N = 1000000


# два способа дифференцирования, параметры: функция; точка, в которой ищем значение
def derivative1(func, x):
    return (func(x + H) - func(x)) / H


def derivative2(func, x):
    return (func(x + H) - func(x - H)) / (2 * H)


# три способа интегрирования, параметры: функция; точка первой границы отрезка интегрирования; точка второй границы
def integral1(func, a, b):
    if a >= b:
        raise Exception("Illegal parameters: a should be < b")
    h = (b - a) / N
    res = 0
    for i in range(0, N):
        res += func(a + i * h) * h
    return res


def integral2(func, a, b):
    if a >= b:
        raise Exception("Illegal parameters: a should be < b")
    h = (b - a) / N
    res = 0
    for i in range(0, N):
        res += (func(a + i * h) + func(a + (i + 1) * h)) * h / 2
    return res


def integral3(func, a, b):
    if a >= b:
        raise Exception("Illegal parameters: a should be < b")
    h = (b - a) / N
    res = 0
    for i in range(0, N):
        res += (func(a + i * h) + func(a + (i + 1) * h) + 4 * func(a + (i + 0.5) * h)) * h / 6
    return res


# примеры функций, над которыми будем проводить манипуляции
def function1(x): 
    return x**3 + x**2 + x
def function2(x):
    return x**5 * math.exp(x - 1)
# тут пишем то, что хотим посчитать и нажимаем зеленую кнопочку)
print(derivative1(function1, 2))
print(integral3(function1, 1, 2))
