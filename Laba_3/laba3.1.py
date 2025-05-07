import json

while True:
    try:
        with open('animals.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            animals = data['animals']
    except FileNotFoundError:
        print("Файл animals.json не найден")
        continue
    except json.JSONDecodeError:
        print("Ошибка при чтении файла")
        continue

    break

# a
print("Птицы: ")
birds = list(filter(lambda x: x['animal_type'] == 'Bird', animals))
for bird in birds:
    print(f"- {bird['name']} ({bird['latin_name']})")

# b
day_animals = len(list(filter(lambda x: x['active_time'] == 'Diurnal', animals)))
print(f"\nКоличество дневных животных: {day_animals}")

# c
light_animals = min(animals, key=lambda x: x['weight_min'])
print(f"\nСамое легкое животное: ")
print(f"Название: {light_animals['name']}")
print(f"Вес: {light_animals['weight_min']} кг")
