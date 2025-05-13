def count_repeted_chars(text):
    chars = {}

    for char in text:
        chars[char] = chars.get(char, 0) + 1

    reapeted_chars = sum(1 for count in chars.values() if count > 1)

    return reapeted_chars


def main():
    user_input = input("Введите слово: ")
    print(f"Количество повторяющихся букв в слове {user_input}: {count_repeted_chars(user_input)}")


if __name__ == "__main__":
    main()
