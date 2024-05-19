import os
from PIL import Image

direct = "8lab2picture"

otkritka = {
    "Новый год": "newyear.jpg",
    "Рождество": "christmas.jpg",
    "8 Марта": "womens.jpg",
    "9 Мая": "9may.jpg",
    "1 Сентября": "oneseptember.jpg"
}

def show_otkritka(holiday):
    if holiday in otkritka:
        image_path = os.path.join(direct, otkritka[holiday])
        try:
            with Image.open(image_path) as img:
                img.show()
        except FileNotFoundError:
            print(f"Файл {image_path} не найден.")
    else:
        print(f"Открытка для праздника '{holiday}' не найдена.")

for holiday in otkritka.keys():
    print(f"- {holiday}")
holiday = input("Введите название праздника: ")
show_otkritka(holiday)
