from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is not None:
            exif = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                exif[tag_name] = value
            return exif
        else:
            print("Resimde EXIF verisi bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def get_lat_lon(exif_data):
    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        lat_ref = gps_info[1]
        lat_degrees = gps_info[2][0][0] / gps_info[2][0][1]
        lat_minutes = gps_info[2][1][0] / gps_info[2][1][1]
        lat_seconds = gps_info[2][2][0] / gps_info[2][2][1]

        lon_ref = gps_info[3]
        lon_degrees = gps_info[4][0][0] / gps_info[4][0][1]
        lon_minutes = gps_info[4][1][0] / gps_info[4][1][1]
        lon_seconds = gps_info[4][2][0] / gps_info[4][2][1]

        latitude = lat_degrees + (lat_minutes / 60.0) + (lat_seconds / 3600.0)
        if lat_ref == 'S':
            latitude = -latitude

        longitude = lon_degrees + (lon_minutes / 60.0) + (lon_seconds / 3600.0)
        if lon_ref == 'W':
            longitude = -longitude

        return latitude, longitude
    else:
        print("GPS bilgisi bulunamadı.")
        return None, None

if __name__ == "__main__":
    image_path = input("Lütfen fotoğrafın yolunu girin: ")
    exif_data = get_exif_data(image_path)
    if exif_data:
        latitude, longitude = get_lat_lon(exif_data)
        if latitude is not None and longitude is not None:
            print("Enlem ve boylam değerleri:", latitude, longitude)
        else:
            print("Enlem ve boylam değerleri alınamadı.")
