with open('txt.txt', 'w', encoding='utf-8') as f:
    sum = 0
    num = input('Enter the numbers with space')
    for el in num.split():
        sum += int(el)
    f.write(num)
print(sum)
