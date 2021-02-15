file_path = '../text_files/learning_python.txt'

#скрипт выводит строки из текстового файла по одной строке,
# ищет и заменяет одно слово в каждой строке и выводит результат на экран

with open(file_path) as file:
    for line in file:
        print(line.rstrip().replace('Python', 'C'))