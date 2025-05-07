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
    
    # Создаём тепловую карту
    fig = px.imshow(
        df[headers[1:]].values,
        x=headers[1:],  # Названия показателей (столбцы)
        y=countries,    # Названия стран (строки)
        color_continuous_scale="Viridis",
        title="Тепловая карта показателей стран",
        labels=dict(x="Показатель", y="Страна", color="Значение")
    )
    
    fig.update_layout(
        xaxis_title="Показатель",
        yaxis_title="Страна"
    )
    
    fig.show()

if __name__ == "__main__":
    main()
