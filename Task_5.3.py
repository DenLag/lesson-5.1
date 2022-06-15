with open('for_task_5.3.txt', 'r', encoding='utf-8') as f:
    list = ()
    flag = True
    for line in f:
        list = line.split("\t")
        if int(list[1]) < 20000:
            print(list[0])
            flag = False
    if flag:
        print('Сотрудники с окладом менее 20000 отсутствуют')
    else:
        print('Выше указан список сотрудников с окладом менее 20000')
