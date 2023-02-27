if __name__ == '__main__':
    # читаємо англо-український словник з файлу
    with open('english_ukrainian_dict.txt', 'r') as f:
        english_to_ukrainian = {}
        for line in f:
            # розділяємо рядок на англійське слово та його українські значення
            english_word, *ukrainian_words = line.strip().split(';')
            # додаємо запис до словника
            english_to_ukrainian[english_word] = ukrainian_words

    # створюємо українсько-англійський словник
    ukrainian_to_english = {}
    for english_word, ukrainian_words in english_to_ukrainian.items():
        for ukrainian_word in ukrainian_words:
            if ukrainian_word in ukrainian_to_english:
                ukrainian_to_english[ukrainian_word].append(english_word)
            else:
                ukrainian_to_english[ukrainian_word] = [english_word]

    # сортуємо словник за ключами
    ukrainian_to_english_sorted = dict(sorted(ukrainian_to_english.items()))

    # записуємо українсько-англійський словник у файл
    with open('ukrainian_english_dict.txt', 'w') as f:
        for ukrainian_word, english_words in ukrainian_to_english_sorted.items():
            f.write(f"{ukrainian_word};{';'.join(english_words)}\n")