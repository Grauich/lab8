import os
from PIL import Image, ImageDraw, ImageFont

direct = "8lab2picture"

otkritka = {
    "Новый год": "newyear.jpg",
    "Рождество": "christmas.jpg",
    "8 Марта": "womens.jpg",
    "9 Мая": "9may.jpg",
    "1 Сентября": "oneseptember.jpg"
}

def show_otkritka(holiday, name):
    if holiday in otkritka:
        image_path = os.path.join(direct, otkritka[holiday])
        try:
            with Image.open(image_path) as img:
                draw = ImageDraw.Draw(img)

                font_path = "/Library/Fonts/Arial.ttf"  # Путь к шрифту Arial на macOS
                font_size = 36
                font = ImageFont.truetype(font_path, font_size)

                text = f"{name}, поздравляшки!!"

                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]

                width, height = img.size
                x = (width - text_width) / 2
                y = height - text_height - 10

                draw.text((x, y), text, font=font, fill="red")
                output_path = f"congratulation_{holiday}.png"
                img.save(output_path)
                img.show()
                
                print(f"Открытка сохранена как {output_path}")

        except FileNotFoundError:
            print(f"Файл {image_path} или шрифт {font_path} не найден.")
    else:
        print(f"Открытка для праздника '{holiday}' не найдена.")


print("Доступные открытки:")
for holiday in otkritka.keys():
    print(f"- {holiday}")
holiday = input("Введите название праздника: ")
name = input("Введите имя: ")
show_otkritka(holiday, name)
