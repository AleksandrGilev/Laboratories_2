import csv


def read_countries():
    with open('countries.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)


def write_to_csv(filename, data, header):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


def filter_by_income_range(countries, min_income, max_income):
    return list(filter(
        lambda x: min_income <= float(x[2]) <= max_income,
        countries
    ))


def sort_by_inflation(countries):
    return sorted(countries, key=lambda x: float(x[3]))


def main():
    countries = read_countries()


    try:
        # Задача a: Фильтрация по диапазону доходов
        min_income = float(input("Введите минимальный доход: "))
        max_income = float(input("Введите максимальный доход: "))

        filtered_countries = filter_by_income_range(countries, min_income, max_income)
        header = ["Country", "Health Care", "Income", "Inflation", "Life Expectancy"]
        write_to_csv('filtered_by_income.csv', filtered_countries, header)
        print("Файл filtered_by_income.csv успешно создан")

        # Задача b: Сортировка по инфляции
        sorted_countries = sort_by_inflation(countries)
        write_to_csv('sorted_by_inflation.csv', sorted_countries, header)
        print("Файл sorted_by_inflation.csv успешно создан")

    except ValueError:
        print("Ошибка: Введите корректные числовые значения")


if __name__ == "__main__":
    main()
