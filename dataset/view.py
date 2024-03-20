from osgeo import gdal, ogr, osr

# 设置栅格数据文件路径
raster_file = "C:/Users/qk516/Desktop/data3/sat/sat_14.tif"

# 设置矢量数据文件路径
vector_file = "C:/Users/qk516/Desktop/data3/mask/mask_14.shp"

# 设置输出图片文件路径
output_image = "C:/Users/qk516/Desktop/data3/view.shp"

try:
    # 打开栅格数据
    raster_ds = gdal.Open(raster_file)

    # 获取栅格数据的地理参考信息
    raster_proj = raster_ds.GetProjection()
    raster_geo = raster_ds.GetGeoTransform()

    # 打开矢量数据
    vector_ds = ogr.Open(vector_file)
    layer = vector_ds.GetLayer()

    # 创建空白图片
    driver = gdal.GetDriverByName('ESRI Shapefile')
    output_ds = driver.Create(output_image, raster_ds.RasterXSize, raster_ds.RasterYSize, 3)

    if output_ds is None:
        raise RuntimeError("Failed to create output image.")

    # 将栅格数据写入图片
    for i in range(1, 4):
        band = raster_ds.GetRasterBand(i)
        output_ds.GetRasterBand(i).WriteArray(band.ReadAsArray())

    # 设置地理参考信息
    output_ds.SetProjection(raster_proj)
    output_ds.SetGeoTransform(raster_geo)

    # 获取图片的地理信息
    spatial_ref = osr.SpatialReference()
    spatial_ref.ImportFromWkt(raster_proj)

    # 创建矢量数据的图层
    output_layer = output_ds.CreateLayer("layer", spatial_ref, ogr.wkbPolygon)

    if output_layer is None:
        raise RuntimeError("Failed to create output layer.")
    else:
        print("Output layer created successfully.")

        # 定义图层字段
    layer_defn = layer.GetLayerDefn()
    for i in range(layer_defn.GetFieldCount()):
        output_layer.CreateField(layer_defn.GetFieldDefn(i))

    # 将矢量数据写入图片
    for feature in layer:
        output_layer.CreateFeature(feature)

    print("图片已生成：", output_image)

except Exception as e:
    print("Error:", e)

finally:
    # 关闭数据集
    if raster_ds is not None:
        raster_ds = None
    if vector_ds is not None:
        vector_ds = None
    if output_ds is not None:
        output_ds = None
