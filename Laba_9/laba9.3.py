def count_repeated_chars(text):
    char_count = {}
    
    # Подсчитываем количество каждого символа
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Подсчитываем количество символов, которые встречаются более одного раза
    repeated_chars = sum(1 for count in char_count.values() if count > 1)
    
    return repeated_chars

# Тестовые примеры
def test_count_repeated_chars():
    # Тест 1: строка с повторяющимися символами
    assert count_repeated_chars("hello") == 1  # 'l' повторяется 2 раза
    
    # Тест 2: строка без повторений
    assert count_repeated_chars("python") == 0
    
    # Тест 3: строка с несколькими повторяющимися символами
    assert count_repeated_chars("programming") == 2  # 'r' и 'g' повторяются
    
    # Тест 4: пустая строка
    assert count_repeated_chars("") == 0
    
    # Тест 5: строка с пробелами
    assert count_repeated_chars("hello world") == 2  # 'l' и 'o' повторяются
    
    print("Все тесты пройдены успешно!")

# Запуск тестов
if __name__ == "__main__":
    test_count_repeated_chars()
    
    # Дополнительные примеры использования
    print(f"Количество повторяющихся символов в 'hello': {count_repeated_chars('hello')}")
    print(f"Количество повторяющихся символов в 'python': {count_repeated_chars('python')}")
    print(f"Количество повторяющихся символов в 'programming': {count_repeated_chars('programming')}")
