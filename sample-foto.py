from PIL import Image
from PIL.ExifTags import TAGS

# Fotoğrafın adını ve yolunu belirtin
foto_yolu = "deneme.jpg"

# Fotoğraftan EXIF bilgilerini al
def exif_bilgisi_oku(foto_yolu):
    exif_dict = {}
    im = Image.open(foto_yolu)
    info = im._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_dict[decoded] = value
    return exif_dict

exif_bilgileri = exif_bilgisi_oku(foto_yolu)
exif_bilgileri

# Latitude ve Longitude değerlerini al
latitude = None
longitude = None
if 'GPSInfo' in exif_bilgileri:
    gps_info = exif_bilgileri['GPSInfo']
    if gps_info:
      #(38.0, 19.0, 27.27)
      # (26.0, 45.0, 1.58)
      # 38°19'27.3"N 26°45'01.6"E
        latitude_ref = gps_info[1]
        latitude_degrees = gps_info[2][0]
        latitude_minutes = gps_info[2][1]
        latitude_seconds = gps_info[2][2]
        latitude_calculate = float(latitude_degrees + latitude_minutes / 60 + latitude_seconds / 3600)

        latitude = latitude_calculate if latitude_ref == 'N' else -latitude_calculate

        longitude_ref = gps_info[3]
        longitude_degrees = gps_info[4][0]
        longitude_minutes = gps_info[4][1]
        longitude_seconds = gps_info[4][2]
        longitude_calculate = float(longitude_degrees + longitude_minutes / 60 + longitude_seconds / 3600)
        longitude = longitude_calculate if longitude_ref == 'E' else -longitude_calculate

        location = (latitude,longitude)