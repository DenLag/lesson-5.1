with open('txt.txt', 'r', encoding='utf-8') as f:
    index = 1
    for line in f:
        num_word = len(line.split(" "))
        print(f'Строка {index} содержит {num_word} слов')
        index += 1
