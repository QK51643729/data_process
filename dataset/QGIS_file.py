import os
from qgis.core import QgsProject, QgsMapLayer, QgsRectangle

# 设置QGIS项目文件路径
project_path = r"C:\Path\To\Your\QGIS\Project.qgs"

# 加载QGIS项目文件
project = QgsProject.instance()
project.read(project_path)

# 获取所有图层
layers = project.mapLayers()

# 设置要导出的范围
extent_list = [
    QgsRectangle(xmin1, ymin1, xmax1, ymax1),
    QgsRectangle(xmin2, ymin2, xmax2, ymax2),
    # 添加更多的范围...
]

# 遍历图层
for layer_id, layer in layers.items():
    # 检查图层是否可见
    if layer.isVisible():
        # 遍历要导出的范围
        for i, extent in enumerate(extent_list):
            # 设置图层的过滤器
            layer.setSubsetString('"geometry" intersects {}'.format(extent.asWkt()))
            # 创建导出文件名
            output_file = "Export_{}_{}.shp".format(layer.name(), i)
            # 导出图层数据
            QgsVectorFileWriter.writeAsVectorFormat(layer, output_file, "UTF-8", layer.crs(), "ESRI Shapefile")

# 移除过滤器
for layer_id, layer in layers.items():
    layer.removeSubsetString()

# 保存QGIS项目
project.write()
