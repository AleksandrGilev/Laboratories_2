import csv
import plotly.express as px
import pandas as pd


def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return headers, data


def main():
    headers, data = load_data("data_country.csv")

    countries = [row[0] for row in data]

    df = pd.DataFrame(data, columns=headers)

    for col in headers[1:]:
        df[col] = df[col].astype(float)

    # Создаём отдельную тепловую карту для каждого показателя
    metrics = headers[1:]

    for metric in metrics:
        # Создаем тепловую карту для текущего показателя
        fig = px.imshow(
            df[metric].values.reshape(-1, 1),  # Преобразуем в матрицу Nx1
            y=countries,  # Названия стран
            x=[metric],  # Название показателя
            color_continuous_scale="Hot",  # Цветовая схема тепловой карты (Viridis, Plasma, Turbo, Inferno)
            title=f"Тепловая карта показателя '{metric}' по странам",
            labels=dict(y="Страна", color="Значение")
        )

        fig.update_layout(
            height=800,  # Увеличиваем высоту для лучшей читаемости
            xaxis_title="Показатель",
            yaxis_title="Страна"
        )

        fig.show()


if __name__ == "__main__":
    main()
