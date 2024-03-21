from PIL import Image
from PIL.ExifTags import TAGS

# Fotoğrafın adını ve yolunu belirtin
foto_yolu = "sample.jpg"

# Fotoğraftan EXIF bilgilerini al




import cv2
import requests
import numpy as np
import pytesseract

# Tesseract OCR'nin kurulu olduğundan emin olun
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract'in yolunu doğru şekilde belirtin

# Resmi URL'den al
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Elongated_circle_58.svg/1200px-Elongated_circle_58.svg.png"
response = requests.get(url)
img_array = np.array(bytearray(response.content), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)

# Resmi gri tonlamalıya dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azalt
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenarları tespit et
edges = cv2.Canny(blur, 50, 150)

# Konturları bul
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kontur alanlarına göre sırala ve en büyük olanı al
max_contour = max(contours, key=cv2.contourArea)

# Konturun bir dikdörtgen sınırlayıcısını al
x, y, w, h = cv2.boundingRect(max_contour)

# Sayıyı kes
roi = img[y:y+h, x:x+w]

# Kesilen alanı OCR ile oku
sayi = pytesseract.image_to_string(roi, config='--psm 6')

# Değeri göster
if sayi:
    print("Okunan Sayı:", sayi.strip())
else:
    print("Sayı bulunamadı.")
