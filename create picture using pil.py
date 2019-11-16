# Challenge:
# 11. Create an image from code (png file) Hint:
# use Pillow

from PIL import Image, ImageDraw, ImageFont

def image_char(mytext, image_size, font_size):
    text=hebrew_text(mytext)
    img = Image.new("RGB", (image_size, image_size), color='black')
    print(img.getpixel((0, 0)))
    draw = ImageDraw.Draw(img)
    font_path = "C:\\Windows\\Fonts\\David\\davidbd.ttf"
    font = ImageFont.truetype(font_path, font_size,encoding='utf-8' )
    draw.text((250, 20), text, fill='blue', font=font)
    img.save("custom.png", "PNG")
    img.show()

# מאחר והעברית נכתבת הפוך, הפונקציה תהפוך את העברית ע"מ שתוצג כמצופה
# בכתיבה באנגלית יש לוותר על הפונקציה הנ"ל
def hebrew_text (text):
    text = text[::-1]
    return text

# hebrew text, image size, font size
image_char("התמונה הראשונה שלי",700,36)