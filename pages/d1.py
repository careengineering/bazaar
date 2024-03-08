# my libs


import cv2
import pytesseract

def recognize_digits(image_path):
  """
  Fotoğraftaki el yazısı rakamları tanır.

  Parametreler:
    image_path: Fotoğrafın dosya yolu.

  Dönüş Değeri:
    Tanınan rakamlar (list).
  """
  import pytesseract

  pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

  img = cv2.imread(image_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
  morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
  digits = pytesseract.image_to_string(morph, config="--psm 7 --oem 3")
  return [int(d) for d in digits if d.isdigit()]




photo_url = "img/sample1.JPG"  # Fotoğraf yolunu belirtin



digits = recognize_digits(photo_url)

print("El Yazısı Rakamlar:", digits)
