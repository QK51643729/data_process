from arcgis.mapping import WebMap

# 设置WMTS服务的URI
wmts_uri = "https://wayback.maptiles.arcgis.com/arcgis/rest/services/World_Imagery/WMTS/1.0.0/default028mm/MapServer/tile/31144/%7Blevel%7D/%7Brow%7D/%7Bcol%7D"

# 创建Web地图对象
webmap = WebMap(wmts_uri)

# 设置要导出的范围
extent_list = [
    {
        "xmin": 12950224.0129411,
        "ymin": 4849764.11491491,
        "xmax": 12961354.3324861,
        "ymax": 4865855.14612848
    }
]

# 遍历要导出的范围
for i, extent in enumerate(extent_list):
    # 设置地图的范围
    webmap.extent = extent
    # 创建导出文件名
    output_file = "Export_{}.tif".format(i)
    # 导出地图为TIFF格式
    webmap.export_map(image_format='TIFF', export_format='image', save_folder='./test_sat/',
                      save_file=output_file)
