file_path = '../text_files/learning_python.txt'

with open(file_path) as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())