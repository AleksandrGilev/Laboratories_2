import csv
from docxtpl import DocxTemplate


def main():
    doc = DocxTemplate("template.docx")
    with open("data_marathon.csv", "r", encoding="utf-8") as file:
        row_data = list(csv.DictReader(file))

    print("Загруженные данные:", row_data)

    data = {}

    for item in row_data:
        year = item["year"]
        city = item["city"]
        if year not in data:
            data[year] = {}
        if city not in data[year]:
            data[year][city] = {"Male": None, "Female": None}

        gender = item["gender"]
        if data[year][city][gender] is None or item["time"] < data[year][city][gender]["time"]:
            data[year][city][gender] = {
                "name": item["name"],
                "time": item["time"]
            }

    print("Обработанные данные:", data)

    context = {
        "data": data
    }

    print("Контекст для рендеринга:", context)
    doc.render(context)
    doc.save("result.docx")


if __name__ == "__main__":
    main()
