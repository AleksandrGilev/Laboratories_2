import csv
import statistics

def read_buildings_data():
    """Чтение данных из CSV файла"""
    with open('data_tallest_buildings.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Пропускаем заголовок
        buildings = list(reader)
    return buildings, header

def analyze_buildings():
    buildings, header = read_buildings_data()
    
    # Преобразуем строковые данные в числовые, где это необходимо
    for building in buildings:
        building[1] = float(building[1])  # высота
        building[2] = int(building[2])    # год
        building[3] = int(building[3])    # надземные этажи
        building[4] = int(building[4])    # подземные этажи
    
    # a. 5 самых высоких и 5 самых низких зданий
    buildings_by_height = sorted(buildings, key=lambda x: x[1], reverse=True)
    tallest_buildings = buildings_by_height[:5]
    shortest_buildings = buildings_by_height[-5:]
    
    print("a. 5 самых высоких зданий:")
    for building in tallest_buildings:
        print(f"{building[0]}: {building[1]} м")
    
    print("\n5 самых низких зданий из списка:")
    for building in reversed(shortest_buildings):
        print(f"{building[0]}: {building[1]} м")
    
    # b. Минимальная, максимальная, средняя и медианная высоты
    heights = [building[1] for building in buildings]
    min_height = min(heights)
    max_height = max(heights)
    avg_height = sum(heights) / len(heights)
    median_height = statistics.median(heights)
    
    print("\nb. Статистика по высоте зданий:")
    print(f"Минимальная высота: {min_height} м")
    print(f"Максимальная высота: {max_height} м")
    print(f"Средняя высота: {avg_height:.2f} м")
    print(f"Медианная высота: {median_height} м")
    
    # c. Количество стран
    countries = set(building[6] for building in buildings)
    print(f"\nc. Количество стран: {len(countries)}")
    
    # d. Самое старое и самое новое здание
    buildings_by_year = sorted(buildings, key=lambda x: x[2])
    oldest_year = buildings_by_year[0][2]
    newest_year = buildings_by_year[-1][2]
    
    oldest_buildings = [building for building in buildings if building[2] == oldest_year]
    newest_buildings = [building for building in buildings if building[2] == newest_year]
    
    print("\nd. Самые старые здания:")
    for building in oldest_buildings:
        print(f"{building[0]}, {building[2]} год, {building[6]}")
    
    print("\nСамые новые здания:")
    for building in newest_buildings:
        print(f"{building[0]}, {building[2]} год, {building[6]}")
    
    # e. Здания с суммарным количеством этажей больше указанного
    try:
        floor_threshold = int(input("\nВведите минимальное суммарное количество этажей: "))
        filtered_buildings = [building for building in buildings 
                            if building[3] + building[4] > floor_threshold]
        
        print(f"\ne. Здания с суммарным количеством этажей больше {floor_threshold}:")
        print(f"{'Название':<40} | {'Высота (м)':<10} | {'Надземных':<10} | {'Подземных':<10} | {'Всего':<6} | {'Город':<15} | {'Страна'}")
        print("-" * 110)
        
        for building in filtered_buildings:
            total_floors = building[3] + building[4]
            print(f"{building[0]:<40} | {building[1]:<10} | {building[3]:<10} | {building[4]:<10} | {total_floors:<6} | {building[5]:<15} | {building[6]}")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")
    
    # f. Здания, построенные в указанный год
    try:
        year = int(input("\nВведите год постройки для поиска зданий: "))
        buildings_in_year = [building for building in buildings if building[2] == year]
        
        if buildings_in_year:
            print(f"\nf. Здания, построенные в {year} году:")
            for building in buildings_in_year:
                print(f"{building[0]}, {building[1]} м, {building[5]}, {building[6]}")
        else:
            print(f"\nf. Зданий, построенных в {year} году, в списке нет.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")
    
    # g. Количество зданий по странам
    buildings_by_country = {}
    for building in buildings:
        country = building[6]
        if country in buildings_by_country:
            buildings_by_country[country] += 1
        else:
            buildings_by_country[country] = 1
    
    print("\ng. Количество зданий по странам:")
    for country, count in sorted(buildings_by_country.items(), key=lambda x: x[1], reverse=True):
        print(f"{country}: {count}")

if __name__ == "__main__":
    analyze_buildings() 