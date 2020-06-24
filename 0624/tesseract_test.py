from PIL import Image
from pytesseract import *

filename = "images/tesseract_test2.jpg"
image = Image.open(filename)
text = image_to_string(image, lang="kor")
print("sung: ",text)
