import urllib

import ee
import folium
from IPython.core.display_functions import display

ee.Authenticate()
# 初始化 Earth Engine
ee.Initialize(project='ee-qk51643729')
lon1, lat1, lon2, lat2 = 116.34, 116.44, 39.89, 40
# 定义区域（这里是一个范例，可以根据需要修改）
region = ee.Geometry.Rectangle([lon1, lat1, lon2, lat2])

dataset = (ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
           .filterBounds(region)
           .filterDate('2022-01-01', '2022-01-05'))

# 获取图像列表
imageList = dataset.toList(dataset.size())

# 输出图像数量
print("Number of images in the collection:", imageList.size().getInfo())

# 检查是否有图像可用
if imageList.size().getInfo() > 0:
    # 选择第一张图像
    image = ee.Image(imageList.get(0))

    # 在地图上显示图像
    map = folium.Map(location=[(lat1 + lat2) / 2, (lon1 + lon2) / 2], zoom_start=10)

    # 将图像叠加在地图上
    mapid = image.getMapId({'bands': ['B4', 'B3', 'B2'], 'max': 0.3})
    folium.TileLayer(
        tiles=mapid['tile_fetcher'].url_format,
        attr='Google Earth Engine',
        overlay=True,
        name='image',
    ).add_to(map)
    url = mapid['tile_fetcher'].url_format
    urllib.request.urlretrieve(url, 'output_image.png')
    print("Image saved to 'output_image.png'.")
else:
    print("No images available for the specified region and date range.")
