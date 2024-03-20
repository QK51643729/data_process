import os

import geopandas as gpd
import matplotlib.pyplot as plt

shapefile_path = "E:/trajectory_data/map/transferred.shp"
output_path = 'C:/Users/qk516/Desktop/testdata/test_map.png'
width_column = 'WIDTH'  # 替换为实际Shapefile中的宽度属性列名
bounding_box = (116.3467234049113, 39.94830251169769, 116.35187588227653, 39.95224154368673)

shapefile = gpd.read_file(shapefile_path)


def width_expression(width_value):
    # 自定义宽度表达式
    width_value = int(width_value)
    if width_value == 15:
        return 1.5
    elif width_value == 30:
        return 3
    elif width_value == 55:
        return 5.5
    elif width_value == 130:
        return 13
    else:
        return 0.0


def export_map_with_width(shape, output_path, width_column, bbox):
    # 读取Shapefile文件
    # gdf = gpd.read_file(shapefile_path)

    minx, miny, maxx, maxy = bbox
    filtered_gdf = shapefile.cx[minx:maxx, miny:maxy]

    # 创建画布
    fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)

    # 设置画布背景为黑色
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # 绘制地图，根据宽度表达式设置线的宽度
    filtered_gdf.apply(
        lambda x: ax.plot(x.geometry.xy[0], x.geometry.xy[1], linewidth=width_expression(x[width_column]),
                          color='white'), axis=1)

    # 隐藏坐标轴
    ax.axis('off')

    # 调整保存图像的尺寸
    plt.tight_layout()
    file_name = f"{minx}_{miny}_{maxx}_{maxy}.png"

    # 保存图像为512x512像素
    plt.savefig(os.path.join(output_folder, file_name), dpi=100, bbox_inches='tight', pad_inches=0, transparent=True)
    # plt.show()
    plt.close()


photo_folder = "C:/Users/qk516/Desktop/testdata/clipped/"
output_folder = "C:/Users/qk516/Desktop/testdata/ground_truth/"
for photo_file in os.listdir(photo_folder):
    if photo_file.endswith(".jpg"):
        bbox_info = os.path.splitext(photo_file)[0].split("_")
        bounding_box = tuple(map(float, bbox_info))
        export_map_with_width(shapefile, output_path, width_column, bounding_box)
