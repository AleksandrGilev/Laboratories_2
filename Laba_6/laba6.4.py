import csv

def read_courses():
    with open('udemy_courses.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def analyze_courses():
    courses = read_courses()
    
    total_price = 0
    min_subscribers = float('inf')
    max_duration = 0
    levels = {}
    
    for course in courses:
        # a. Сумма цен для расчета средней
        price = float(course[1])
        total_price += price
        
        # b. Минимальное число подписчиков
        subscribers = int(course[2])
        min_subscribers = min(min_subscribers, subscribers)
        
        # c. Максимальная продолжительность лекций
        duration = float(course[5])
        max_duration = max(max_duration, duration)
        
        # d. Подсчет курсов по уровням
        level = course[4]
        if level in levels:
            levels[level] += 1
        else:
            levels[level] = 1
    
    avg_price = total_price / len(courses)
    
    # Находим наиболее популярный уровень
    most_popular_level = max(levels, key=levels.get)
    
    print(f"a. Средняя цена на курс: {avg_price:.2f}$")
    print(f"b. Минимальное число подписчиков: {min_subscribers}")
    print(f"c. Максимальная продолжительность лекций: {max_duration} часов")
    print(f"d. Уровень, для которого было создано наибольшее количество курсов: {most_popular_level} ({levels[most_popular_level]} курсов)")
    
    # Дополнительная информация о распределении курсов по уровням
    print("\nРаспределение курсов по уровням:")
    for level, count in sorted(levels.items(), key=lambda x: x[1], reverse=True):
        print(f"{level}: {count} курсов")

if __name__ == "__main__":
    analyze_courses()

