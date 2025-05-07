def is_palindrome(text):
    cleaned_text = ''.join(text.lower().split())
    
    if len(cleaned_text) < 3:
        return False
    
    return cleaned_text == cleaned_text[::-1]

def main():
    # Тестирование функции
    test_cases = [
        "А роза упала на лапу Азора",
        "топот",
        "123321",
        "привет",
        "ав",
        "а",
        ""
    ]
    
    print("Проверка на палиндромы:")
    for text in test_cases:
        result = is_palindrome(text)
        print(f"'{text}': {'Палиндром' if result else 'Не палиндром'}")

if __name__ == "__main__":
    # Тестирование
    main()
    
    # Интерактивный режим
    print("\nВведите строку для проверки (для выхода введите 'выход')")
    while True:
        user_input = input("Строка: ")
        if user_input.lower() == 'выход':
            break
        
        result = is_palindrome(user_input)
        print(f"'{user_input}': {'Палиндром' if result else 'Не палиндром'}")

# Тесты с использованием pytest
import pytest

def test_palindrome_valid():
    """Тест для валидных палиндромов."""
    assert is_palindrome("казак") == True
    assert is_palindrome("А роза упала на лапу Азора") == True
    assert is_palindrome("топот") == True
    assert is_palindrome("123321") == True

def test_palindrome_invalid():
    """Тест для невалидных палиндромов."""
    assert is_palindrome("привет") == False
    assert is_palindrome("пример") == False
    assert is_palindrome("тест") == False

def test_palindrome_short():
    """Тест для строк короче 3 символов."""
    assert is_palindrome("aa") == False
    assert is_palindrome("a") == False
    assert is_palindrome("") == False

def test_palindrome_with_spaces():
    """Тест для палиндромов с пробелами."""
    assert is_palindrome("а роза упала на лапу азора") == True
    assert is_palindrome("  топот  ") == True

def test_palindrome_case_insensitive():
    """Тест на нечувствительность к регистру."""
    assert is_palindrome("КаЗаК") == True
    assert is_palindrome("ТоПоТ") == True

# Для запуска тестов используйте команду:
# pytest laba9.2.py -v
