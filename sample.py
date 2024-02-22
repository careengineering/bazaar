# Import Libraries
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

# Open Image
img=Image.open('img/sample.jpg')

#Get EXIF Data
exif_table={}
for k, v in img.getexif().items():
    tag=TAGS.get(k)
    exif_table[tag]=v

print(exif_table)

gps_info={}
for k, v in exif_table['GPSInfo'].items():
    geo_tag=GPSTAGS.get(k)
    gps_info[geo_tag]=v
print(gps_info)


#Get Latitude and Longitude
lat=gps_info['GPSLatitude']
long=gps_info['GPSLongitude']
#Convert to degrees
lat=float(lat[0]+(lat[1]/60)+(lat[2]/(3600*100)))
long=float(long[0]+(long[1]/60)+(long[2]/(3600*100)))
#Negative if LatitudeRef:S or LongitudeRef:W
if gps_info['GPSLatitudeRef']=='S':
    lat=-lat
if gps_info['GPSLongitudeRef']=='W':
    long=-long


import folium
# Create map
m=folium.Map(location=[lat,long],zoom_start=5, tiles="Stamen Toner") 
# Add Circle Marker
folium.CircleMarker(location=[lat,long],fill=True, color='red',fill_color='red').add_to(m)
# Save Map as HTML file
m.save('map.html')
# View Map
m    