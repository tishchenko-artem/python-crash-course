file_path = 'text_files\learning_python.txt'

with open(file_path) as file:
    for line in file:
        print(line.rstrip())