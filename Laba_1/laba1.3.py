while True:
    try:
        with open('info.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        n = int(input("Введите число N: "))
    except FileNotFoundError:
        with open('info.txt', 'w', encoding='utf-8') as file:
            info = ["Василий 70\nСветлана 90\nАлиса 60"]
            file.writelines(info)
        print("Файл не был найден! Был создан файл info.txt с примерными данными.")
        continue
    except ValueError:
        print("Введено неверное значение N")
        continue
    else:
        break

list = [(line.split()[0], int(line.split()[1])) for line in lines]

sort_name = sorted(list, key=lambda x: x[0])  # по имени
print("Отсортировано по имени:")
for name, score in sort_name:
    print(f"{name} {score}")

sort_score = sorted(list, key=lambda x: x[1], reverse=True)  # по баллам
print("\nОтсортировано по баллам:")
for name, score in sort_score:
    print(f"{name} {score}")

filtered_list = filter(lambda x: x[1] > n, list)  # >N

if not filtered_list:
    print("Нет данных с баллами больше, чем N.")
else:
    with open('res.txt', 'w', encoding='utf-8') as res_file:
        for name, score in filtered_list:
            res_file.write(f"{name} {score}\n")
