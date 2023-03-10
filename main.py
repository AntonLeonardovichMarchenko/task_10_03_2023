"""
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
Вывести цифры числа на каждой строчке.

Найти сумму цифр числа.
Найти произведение цифр числа.
Дать ответ на вопрос: есть ли среди цифр числа 5?
Найти максимальную цифру в числе
Найти количество цифр 5 в числе

"""
import random

def script_0(scriptName, argM, argN):
    m = argM
    n = argN

    print(f'Hi, {scriptName}')
    print(f'm == {m}, n == {n} \n')

    strz = str(0)*m

    for i in range(0, n):
        print(f'{i}   {strz}')


def script_1(scriptName):

    print(f'\nHi, {scriptName}')
    nDigits = 100
    digits = []
    n_5 = 0
    for i in range(0, nDigits):
        digits.append(random.randint(0, 10))

    for i in range(0, nDigits):
        if digits[i] == 5:
            n_5 += 1
    print(f'quantity of 5 is {n_5}')


def script_2(scriptName, n=100):

    print(f'\nHi, {scriptName}')
    N = n
    result = 0
    for i in range(0, N):
        result += i
    print(f'The result of the summ in range(0, {N}) is {result}')

def script_3(scriptName, n = 10):
    print(f'\nHi, {scriptName}')

    digitsArray = []
    N = n + 1

    result = 1
    for i in range(1, N):
        result *= i

    print(f'The result of the product in range(1, {N}) is {result}')

    while result > 0:
        result = result % 10
        result //= 10
        digitsArray.append(result)

    for i in range(len(digitsArray) - 1, -1, -1):
        print(digitsArray[i])

# ========================================================================

def DigitGenerator(n):
    digit = 0
    order = 1
    for i in range(1, n+1):
        r = random.randint(0, 10)
        if order > 1:
            digit += r*order
        else:
            digit += r

        order *= 10

    print(f'digit is {digit}')
    return digit

def DigitParser(res, digitsArray):
    print(f'DigitParser is here {res}')
    while res > 0:
        tmpDg = res % 10
        res //= 10
        digitsArray.append(tmpDg)
    return digitsArray

def getSumm(digitsArray):
    summ = 0
    print(f'=========================')
    for i in range(0, len(digitsArray)):
        summ += digitsArray[i]
        print(f'{digitsArray[i]} +> {summ}')

    print(f'summ is {summ}')
    return summ

def getProd(digitsArray):
    prod = 1
    print(f'=========================')
    for i in range(0, len(digitsArray)):
        if digitsArray[i] > 0:
            prod *= digitsArray[i]
            print(f'{digitsArray[i]} *> {prod}')

    print(f'prod is {prod}')
    return prod

def getNFives(digitsArray):
    nFives = 0
    print(f'=========================')
    for i in range(0, len(digitsArray)):
        print(f'{digitsArray[i]}')
        if digitsArray[i] == 5:
            nFives += 1
            print(f'{digitsArray[i]} *> {nFives}')

    print(f'nFives is {nFives}')
    return nFives

def getMax(digitsArray):
    maxValue = 0
    print(f'=========================')
    for i in range(0, len(digitsArray)):

        if digitsArray[i] > maxValue:
            maxValue = digitsArray[i]
            print(f'{digitsArray[i]} >> {maxValue}')
        else:
            print(f'{digitsArray[i]}')

    print(f'maxValue is {maxValue}')
    return maxValue

def script_00(scriptName, n = 10):
    """
    :param scriptName:
    :param n:
    :return:

    Найти сумму цифр числа.
    Найти произведение цифр числа.
    Дать ответ на вопрос: есть ли среди цифр числа 5?
    Найти максимальную цифру в числе
    Найти количество цифр 5 в числе

    """
    print(f'\nHi, {scriptName}')

    digitsArray = []
    resultDict = dict()

    # генератор числа (число состоит из 10 случайных чисел)
    digit = DigitGenerator(n)

    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~')
    digitsArray = DigitParser(digit, digitsArray)
    print(digitsArray)

    print(f'::::::::::{digit}::::::::::::::::::::::::::::::::::')

    # по мере выполнения функции словарь resultDict заполняется ==========
    # результатами вычислений ============================================
    resultDict['summ is'] = getSumm(digitsArray)
    resultDict['prod is'] = getProd(digitsArray)
    resultDict['nFives is'] = getNFives(digitsArray)
    resultDict['max is'] = getMax(digitsArray)

    print(resultDict)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    script_0('this is script_0', 5, 10)
    script_1('this is script_1')
    script_2('this is script_2')
    script_3('this is script_3')
    # ====================================================================
    # Здесь применяются вспомогательные функции:
    # DigitGenerator, DigitParser, getSumm, getProd, getNFives, getMax
    script_00('this is script_00')

