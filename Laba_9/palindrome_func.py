def palindrome(text):
    cleaned_text = ''.join(text.lower().split())

    if len(cleaned_text) < 3:
        return False

    return cleaned_text == cleaned_text[::-1]


def main():
    user_input = input("Введите првоеряемое слово: ")
    result = palindrome(user_input)
    print(f"{user_input} это {result}")


if __name__ == "__main__":
    main()
