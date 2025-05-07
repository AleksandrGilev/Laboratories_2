import pandas as pd
import numpy as np

def main():
    try:
        df = pd.read_csv('data_tallest_buildings.csv')
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что файл data_tallest_buildings.csv находится в директории программы.")
        return
    
    # a. Найти и вывести 5 самых высоких и 5 самых низких зданий
    print("\nA. 5 САМЫХ ВЫСОКИХ ЗДАНИЙ:")
    print(df.sort_values(by='height_m', ascending=False).head(5)[['name', 'height_m']])
    
    print("\nA. 5 САМЫХ НИЗКИХ ЗДАНИЙ:")
    print(df.sort_values(by='height_m', ascending=True).head(5)[['name', 'height_m']])
    
    # b. Найти минимальную, максимальную, среднюю и медианную высоты зданий
    min_height = df['height_m'].min()
    max_height = df['height_m'].max()
    mean_height = df['height_m'].mean()
    median_height = df['height_m'].median()
    
    print("\nB. СТАТИСТИКА ПО ВЫСОТЕ ЗДАНИЙ:")
    print(f"Минимальная высота: {min_height} м")
    print(f"Максимальная высота: {max_height} м")
    print(f"Средняя высота: {mean_height:.2f} м")
    print(f"Медианная высота: {median_height} м")
    
    # c. Указать количество стран, упомянутых в файле
    unique_countries = df['country'].nunique()
    print(f"\nC. КОЛИЧЕСТВО УПОМЯНУТЫХ СТРАН: {unique_countries}")
    
    # d. Указать самое старое и самое новое здание
    oldest_year = df['year_built'].min()
    newest_year = df['year_built'].max()
    
    oldest_buildings = df[df['year_built'] == oldest_year]
    newest_buildings = df[df['year_built'] == newest_year]
    
    print("\nD. САМЫЕ СТАРЫЕ ЗДАНИЯ:")
    for index, building in oldest_buildings.iterrows():
        print(f"{building['name']}, {building['year_built']} год, {building['city']}, {building['country']}")
    
    print("\nD. САМЫЕ НОВЫЕ ЗДАНИЯ:")
    for index, building in newest_buildings.iterrows():
        print(f"{building['name']}, {building['year_built']} год, {building['city']}, {building['country']}")
    
    # e. Сформировать DataFrame с зданиями, где суммарное количество этажей превышает ввод пользователя
    try:
        floor_threshold = int(input("\nE. Введите минимальное суммарное количество этажей: "))
        # Создаем новый столбец с суммарным количеством этажей
        df['total_floors'] = df['floors_above'] + df['floors_below_ground']
        # Фильтруем здания с суммарным количеством этажей больше порогового значения
        filtered_df = df[df['total_floors'] > floor_threshold][['name', 'total_floors', 'city', 'country']]
        
        print(f"\nЗДАНИЯ С БОЛЕЕ ЧЕМ {floor_threshold} ЭТАЖАМИ:")
        if filtered_df.empty:
            print("Таких зданий не найдено.")
        else:
            print(filtered_df)
    except ValueError:
        print("Ошибка: введите целое число.")
    
    # f. Вывести названия зданий, построенных в год, введенный пользователем
    try:
        year_input = int(input("\nF. Введите год постройки: "))
        year_buildings = df[df['year_built'] == year_input]
        
        print(f"\nЗДАНИЯ, ПОСТРОЕННЫЕ В {year_input} ГОДУ:")
        if year_buildings.empty:
            print(f"Зданий, построенных в {year_input} году, не найдено.")
        else:
            for index, building in year_buildings.iterrows():
                print(f"{building['name']}, {building['city']}, {building['country']}")
    except ValueError:
        print("Ошибка: введите целое число.")
    
    # g. Подсчитать количество зданий по странам
    print("\nG. КОЛИЧЕСТВО ЗДАНИЙ ПО СТРАНАМ:")
    country_counts = df['country'].value_counts()
    for country, count in country_counts.items():
        print(f"{country}: {count}")

if __name__ == "__main__":
    main()
