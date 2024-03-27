import geopandas as gpd
from PIL import Image, ImageDraw
import os
from tqdm import tqdm


# 读取shapefile
# shapefile = gpd.read_file("C:/Users/qk516/Desktop/data3/mask/mask_89.shp")
# trajectory_shapefile = gpd.read_file("C:/Users/qk516/Desktop/data3/trajectory_point/point_89.shp")

# if shapefile.empty:
#     print("Error: No geometry found in shapefile.")
#     exit()
def three_in_one(idx):
    # trajectory_name = f"line_{idx}.shp"
    map_name = f"mask_{idx}.shp"
    sat_name = f"sat_{idx}.tif"
    # trajectory_path = os.path.join(trajectory_dir, trajectory_name)
    map_path = os.path.join(map_dir, map_name)
    sat_path = os.path.join(sat_dir, sat_name)
    shapefile = gpd.read_file(map_path)
    # trajectory_shapefile = gpd.read_file(trajectory_path)
    map_image = Image.open(sat_path)

    # 获取shapefile的范围
    xmin, ymin, xmax, ymax = shapefile.total_bounds
    width, height = map_image.size

    # 计算墨卡托投影坐标到像素坐标的转换比例
    x_range = xmax - xmin
    y_range = ymax - ymin
    x_scale = width / x_range
    y_scale = height / y_range

    image = Image.new('RGBA', (width, height), "black")
    # image.paste(map_image, (0, 0))
    draw = ImageDraw.Draw(image)
    # 将LineString绘制到图像上
    if not shapefile.empty:
        for index, row in shapefile.iterrows():
            if row.geometry.geom_type == 'LineString':
                # 获取线宽度
                line_width = int(int(row['WIDTH']) / 10)
                # 转换墨卡托投影坐标到像素坐标
                coordinates = [(int((x - xmin) * x_scale), int((ymax - y) * y_scale)) for x, y in zip(*row.geometry.xy)]
                # 绘制线条
                draw.line(coordinates, fill='white', width=line_width)

        # for index, row in trajectory_shapefile.iterrows():
        #     if row.geometry.geom_type == 'LineString':
        #         # 转换墨卡托投影坐标到像素坐标
        #         coordinates = [(int((x - xmin) * x_scale), int((ymax - y) * y_scale)) for x, y in zip(*row.geometry.xy)]
        #         # 绘制点
        #         draw.line(coordinates, fill="red", width=1)
        #
        # for index, row in trajectory_shapefile.iterrows():
        #     if row.geometry.geom_type == 'Point':
        #         # 转换墨卡托投影坐标到像素坐标
        #         x = int((row.geometry.x - xmin) * x_scale)
        #         y = int((ymax - row.geometry.y) * y_scale)
        #         # 绘制点
        #         draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill='red')
    # 保存图片
    output_name = f"sat_mask_line_{idx}.png"
    output_path = os.path.join(output_dir, output_name)
    image.save(output_path)


if __name__ == '__main__':
    sat_dir = "C:/Users/qk516/Desktop/data3/sat/"
    # trajectory_dir = "C:/Users/qk516/Desktop/data3/trajectory_line/"
    map_dir = "C:/Users/qk516/Desktop/data3/mask/"
    output_dir = "C:/Users/qk516/Desktop/data3/mask/mask_PIL/"
    test_mask = r"C:\Users\qk516\Desktop\data3\mask\mask_53.shp"
    test_output = r"C:\Users\qk516\Desktop\data3\mask\test\mask_53.png"
    shapefile = gpd.read_file(test_mask)

    xmin, ymin, xmax, ymax = shapefile.total_bounds
    width, height = 800, 800

    # 计算墨卡托投影坐标到像素坐标的转换比例
    x_range = xmax - xmin
    y_range = ymax - ymin
    x_scale = width / x_range
    y_scale = height / y_range

    image = Image.new('RGBA', (width, height), "black")
    # image.paste(map_image, (0, 0))
    draw = ImageDraw.Draw(image)
    # 将LineString绘制到图像上
    if not shapefile.empty:
        for index, row in shapefile.iterrows():
            if row.geometry.geom_type == 'LineString':
                # 获取线宽度
                print("111")
                # 转换墨卡托投影坐标到像素坐标
                coordinates = [(int((x - xmin) * x_scale), int((ymax - y) * y_scale)) for x, y in zip(*row.geometry.xy)]
                # 绘制线条
                draw.line(coordinates, fill='white')

    image.save(test_output)
    # count = len([file for file in os.listdir(sat_dir) if file.endswith("tif")])
    # for i in tqdm(range(count)):
    #     three_in_one(i)
