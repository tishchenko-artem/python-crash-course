while True:
    try:
        a = input('Пожалуйста введите целое число: ')
        b = input('Пожалуйста введите целое число: ')
        c = int(a) + int(b)
        print(c)
    except ValueError:
        print('Вы ввели не число')