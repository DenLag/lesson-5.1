a = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('for_task_5.4.txt', 'r', encoding='utf-8') as f:
    with open('for_task_5.4_1.txt', 'w', encoding='utf-8') as f2:
        for word in f:
            en, *num = word.split()
            f2.write(' '.join([a[en]] + num) + '\n')
