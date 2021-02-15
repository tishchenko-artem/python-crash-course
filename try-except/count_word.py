def count_word(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        count_words = contents.lower().count('the')
        print(count_words)

filename = 'text_files/piece_of_book.txt'
count_word(filename)