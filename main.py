import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
src = ""


def word(img):
    image = cv2.imread("sd19.jpg")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=1)

    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 13)
    cv2.imwrite(src + 'clean.png', image)

    sonuc = pytesseract.image_to_string(Image.open(src + 'clean.png'), lang='en')

    return sonuc


print('Okuma Başladı')
print(' ')
print(word('resim.png'))
print(' ')
print('Okuma Bitti')
