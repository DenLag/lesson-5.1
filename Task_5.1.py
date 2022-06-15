with open('txt.txt', 'w', encoding='utf-8') as f:
    while (line := input('Enter the string')) != '':
        f.write(f"{line}\n")
