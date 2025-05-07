while True:
    try:
        with open('gr.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        n = int(input("Введите число 'N-грамм': "))
    except FileNotFoundError:
        with open('gr.txt', 'w', encoding='utf-8') as file:
            info = ["a b c d e f"]
            file.writelines(info)
        print("Файл не найден! Был создан файл gr.txt с примерными данными.")
        continue
    except ValueError:
        print("Введено неверное значение N")
        continue
    else:
        if n < 0:
            print("Введите положительное число")
            continue
        break

list = [line.strip() for line in lines]

for line in list:
    words = line.split()
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i + n])
        ngrams.append(ngram)
    for ngram in ngrams:
        print(ngram)
