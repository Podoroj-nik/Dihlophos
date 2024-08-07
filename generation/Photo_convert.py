from PIL import Image, ImageDraw


def step_2(color_2, img):
    color = *color_2, 255
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((0, 0, 2629, 698), fill=(color))
    mask = Image.open('data/Mask_1.png')
    img.paste(mask, (0, 0), mask)
    return img


def step_3(color_3, img):
    color = *color_3, 255
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((0, 2804, 2629, 3447), fill=(color))
    mask = Image.open('data/Mask_2.png')
    img.paste(mask, (0, 0), mask)
    return img


def step_4(color_4, Image_5, color_6, color_7, color_8, img):
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((0, 700, 1200, 2800), fill='white')

    color4 = *color_4, 255
    idraw.rectangle((250, 1155, 900, 2600), fill=(color4))

    color6 = *color_6, 255
    idraw.rectangle((250, 760, 900, 850), fill=(color6))

    color7 = *color_7, 255
    idraw.rectangle((250, 900, 900, 1125), fill=(color7))

    color8 = *color_8, 255
    idraw.rectangle((250, 2625, 900, 2760), fill=(color8))

    mask = Image.open('data/Mask_3.png')
    img.paste(mask, (0, 0), mask)

    photo = Image.open(Image_5).convert("RGBA")
    photo = photo.resize((364, 619))
    img.paste(photo, (480, 1224), photo)

    return img


def main(color_1, color_2, color_3, color_4, Image_5, color_6, color_7, color_8):
    img = Image.open('data/background.jpg')
    img = step_2(color_2, img)
    img = step_3(color_3, img)
    img = step_4(color_4, Image_5, color_6, color_7, color_8, img)

    img.save('Razvertka.jpg')
    img = Image.open('Razvertka.jpg')
    img.show()


color_1 = (237, 30, 36)  # Цвет крышки
color_2 = (237, 30, 36)  # Основной цвет
color_3 = (36, 37, 101)  # Дополнительный цвет
color_4 = (36, 37, 101)  # Цвет рамочки с изображением
Image_5 = 'data/toto.jpg'  # Изображение юзера
color_6 = (250, 30, 36)  # Цвет надписи "Для уничтожения"
color_7 = (36, 37, 101)  # Цвет надписи "мух, ос, ..."
color_8 = (250, 30, 36)  # Цвет надписи "универсальный"

main(color_1, color_2, color_3, color_4, Image_5, color_6, color_7, color_8)
