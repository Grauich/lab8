from PIL import Image


# вырезаем кошку с изображения
def crop_image(input_image_path, savepicture, crop_area):
    with Image.open(input_image_path) as img:
        cropped_img = img.crop(crop_area)
        cropped_img.save(savepicture)


picture = "kosh.jpg"
savepicture = "cropped_kosh.jpg"
crop_area = (2000, 1600, 2800, 2400)
crop_image(picture, savepicture, crop_area)
