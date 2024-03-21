import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Sayfa tasarımı
st.title("Fotoğraf Analizi")
st.write("Bu sayfada, çektiğiniz fotoğrafın lokasyon bilgilerini, nesnelerini ve sayılarını analiz edebilirsiniz.")
url="img/sample.JPG"
# Fotoğraf yükleme
uploaded_file = st.file_uploader("Fotoğrafınızı seçin:", type=["jpg", "jpeg", "png"])

# Lokasyon bilgileri
if uploaded_file is not None:
    # Dosyayı geçici bir depolama konumuna kaydetme
    with open("image.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # OpenCV ile fotoğrafı okuma
    image = cv2.imread("image.jpg")

    # EXIF verilerini alma
    exif_data = image.getexif()

    # Enlem ve boylam değerlerini alma
    if exif_data is not None:
        latitude = exif_data.get(_EXIF_GPS_LATITUDE)
        longitude = exif_data.get(_EXIF_GPS_LONGITUDE)

        # Lokasyon bilgilerini gösterme
        if latitude is not None and longitude is not None:
            st.write("**Lokasyon:** {:.6f}, {:.6f}".format(latitude, longitude))
        else:
            st.write("**Lokasyon:** Bilgi bulunamadı.")

# Nesne tespiti
    # YOLOv5 modelini yükleme
    net = cv2.dnn.readNet("yolov5s.onnx")

    # Fotoğrafı ön işleme
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), (0,0,0), swapRB=True, crop=False)

    # Nesneleri tahmin etme
    net.setInput(blob)
    detections = net.forward()

    # Tespit edilen nesneleri gösterme
    for detection in detections:
        class_id = int(detection[0])
        class_name = coco_classes[class_id]
        confidence = detection[2]

        if confidence > 0.5:
            x, y, w, h = detection[3:7]
            left = int(x - w/2)
            top = int(y - h/2)
            right = int(x + w/2)
            bottom = int(y + h/2)

            # Nesne adını ve güven skorunu gösterme
            st.write(f"**Nesne:** {class_name} ({confidence:.2f})")

            # Nesne çerçevesini çizme
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Sayı tanıma
    # Görüntüyü griye dönüştürme
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Otsu eşikleme
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Tesseract ile sayıları tanıma
    text = pytesseract.image_to_string(thresh, config="--psm 6")

    # Tanınan sayıları gösterme
    st.write("**Sayılar:** {}".format(text))

    # İşlemden sonraki görüntüyü gösterme
    st.image(image, caption="İşlemden Sonra")
