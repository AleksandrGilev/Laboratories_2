from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os

def load_image(path):
    if not os.path.isfile(path):
        print("Ошибка: файл не найден.")
        return None
    try:
        return Image.open(path)
    except IOError:
        print("Ошибка: не удалось загрузить изображение.")
        return None

def save_image(image, path):
    image.save(path)
    print(f"Изображение сохранено как {path}")

def reflect_vertical(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def reflect_horizontal(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def reflect_main_diagonal(image):
    return image.transpose(Image.TRANSPOSE)

def reflect_secondary_diagonal(image):
    return image.transpose(Image.TRANSVERSE)

def apply_sepia(image):
    sepia_image = image.convert("RGB")
    width, height = sepia_image.size
    pixels = sepia_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))

    return sepia_image

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def calculate_average_color(image):
    width, height = image.size
    pixels = image.load()

    total_r = total_g = total_b = 0
    num_pixels = width * height

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            total_r += r
            total_g += g
            total_b += b

    avg_r = total_r // num_pixels
    avg_g = total_g // num_pixels
    avg_b = total_b // num_pixels

    return (avg_r, avg_g, avg_b)

def add_text(image, text, position):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text(position, text, font=font, fill=(255, 255, 255))
    return image

def add_shape(image, shape, position):
    draw = ImageDraw.Draw(image)
    if shape == "ellipse":
        draw.ellipse(position, outline="white", width=3)
    elif shape == "rectangle":
        draw.rectangle(position, outline="white", width=3)
    return image

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное целое число.")

def main():
    path = input("Введите путь к изображению: ")
    image = load_image(path)
    if image is None:
        return

    while True:
        print("\nВыберите преобразование:")
        print("a. Отразить изображение по вертикали")
        print("b. Отразить изображение по горизонтали")
        print("c. Отразить изображение по главной диагонали")
        print("d. Отразить изображение по побочной диагонали")
        print("e. Применить фильтр «Сепия»")
        print("f. Увеличить яркость изображения")
        print("g. Уменьшить яркость изображения")
        print("h. Рассчитать и продемонстрировать средний цвет изображения")
        print("i. Добавить текст поверх изображения")
        print("j. Добавить графический примитив")
        print("q. Выйти")

        choice = input("Ваш выбор: ").lower()

        if choice == 'a':
            image = reflect_vertical(image)
        elif choice == 'b':
            image = reflect_horizontal(image)
        elif choice == 'c':
            image = reflect_main_diagonal(image)
        elif choice == 'd':
            image = reflect_secondary_diagonal(image)
        elif choice == 'e':
            image = apply_sepia(image)
        elif choice == 'f':
            factor = get_float_input("Введите коэффициент увеличения яркости: ")
            image = adjust_brightness(image, factor)
        elif choice == 'g':
            factor = get_float_input("Введите коэффициент уменьшения яркости: ")
            image = adjust_brightness(image, 1/factor)
        elif choice == 'h':
            avg_color = calculate_average_color(image)
            print(f"Средний цвет: {avg_color}")
            avg_image = Image.new("RGB", image.size, avg_color)
            avg_image.show()
        elif choice == 'i':
            text = input("Введите текст: ")
            x = get_int_input("Введите координату X: ")
            y = get_int_input("Введите координату Y: ")
            image = add_text(image, text, (x, y))
        elif choice == 'j':
            shape = input("Введите тип примитива (ellipse/rectangle): ")
            x1 = get_int_input("Введите координату X1: ")
            y1 = get_int_input("Введите координату Y1: ")
            x2 = get_int_input("Введите координату X2: ")
            y2 = get_int_input("Введите координату Y2: ")
            image = add_shape(image, shape, (x1, y1, x2, y2))
        elif choice == 'q':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

        save_image(image, "output.png")
        image.show()

if __name__ == "__main__":
    main()
