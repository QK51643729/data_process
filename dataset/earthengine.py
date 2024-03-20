import ee
from shapely.geometry import box
from shapely.geometry.geo import shape
from geopandas import GeoDataFrame
import geemap.core as geemap
from IPython.core.display_functions import display

# Trigger the authentication flow.
ee.Authenticate()

# Initialize the library.
ee.Initialize(project='ee-qk51643729')

# Print the elevation of Mount Everest.
# dem = ee.Image('USGS/SRTMGL1_003')
# xy = ee.Geometry.Point([86.9250, 27.9881])
# elev = dem.sample(xy, 30).first().get('elevation').getInfo()
# print('Mount Everest elevation (m):', elev)
xmin, ymin, xmax, ymax = 116.348890, 39.905371, 116.429171, 39.975728
num_blocks_x, num_blocks_y = 10, 11
block_size_x, block_size_y = (xmax - xmin) / num_blocks_x, (ymax - ymin) / num_blocks_y
region = ee.Geometry.Rectangle([xmin, ymin, xmax, ymax])

# 获取卫星图像
image = (
    ee.ImageCollection('LANDSAT/LC08/C02/T1')
    .filterBounds(region)
    .filterDate('2022-01-01', '2022-01-31')
    .median()
)
# 获取区域的几何信息
geometry = image.geometry()

# 将几何信息转换为Shapely对象
shapely_geometry = shape(geometry.getInfo())

# 将区域分割成若干矩形块
blocks = []
for i in range(num_blocks_x):
    for j in range(num_blocks_y):
        block_extent = box(
            shapely_geometry.bounds[0] + i * block_size_x,
            shapely_geometry.bounds[1] + j * block_size_y,
            shapely_geometry.bounds[0] + (i + 1) * block_size_x,
            shapely_geometry.bounds[1] + (j + 1) * block_size_y
        )
        blocks.append(block_extent)

# 创建GeoDataFrame以存储矩形块
gdf = GeoDataFrame(geometry=blocks)

# 将GeoDataFrame保存为Shapefile或其他格式
gdf.to_file("C:/Users/qk516/Desktop/testdata/test.shp")
