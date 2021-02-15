try:
    file_path_1 = 'text_files/cats.txt'

    with open(file_path_1) as file:
        for line in file:
            print(line.rstrip())

except FileNotFoundError:
    print('Извините, но ваш файл не найден')