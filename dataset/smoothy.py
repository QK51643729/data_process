import os

import cv2
import geopandas as gpd
from PIL import Image, ImageDraw
import numpy as np
from tqdm import tqdm

# image = cv2.imread(r"C:\Users\qk516\Desktop\data3\sat\sat_0.tif")
# gdf = gpd.read_file(r"C:\Users\qk516\Desktop\data3\mask\mask_0.shp")


# def draw_mask(idx):
#     map_name = f"mask_{idx}.shp"
#     sat_name = f"sat_{idx}.tif"
#     traj_point_name = f"point_{idx}.shp"
#     map_path = os.path.join(mask_shp_dir, map_name)
#     sat_path = os.path.join(sat_dir, sat_name)
#     traj_point_path = os.path.join(traj_point_shp_sir, traj_point_name)
#
#     image = Image.open(sat_path)
#     image1 = cv2.imread(sat_path)
#     traj = gpd.read_file(traj_point_path)
#     map = gpd.read_file(map_path)
#
#     xmin, ymin, xmax, ymax = traj.total_bounds
#     width, height = image.size
#
#     # 计算墨卡托投影坐标到像素坐标的转换比例
#     x_range = xmax - xmin
#     y_range = ymax - ymin
#     x_scale = width / x_range
#     y_scale = height / y_range
#
#     height, width, _ = image1.shape
#     image_blank = np.zeros((height, width), dtype=np.uint8)  # 创建一个空白图像
#     image = Image.new('RGBA', (width, height), "black")
#     # image.paste(map_image, (0, 0))
#     draw = ImageDraw.Draw(image)
#
#     # 画轨迹点
#     for index, row in traj.iterrows():
#         if row.geometry.geom_type == 'Point':
#             # 转换墨卡托投影坐标到像素坐标
#             x = int((row.geometry.x - xmin) * x_scale)
#             y = int((ymax - row.geometry.y) * y_scale)
#             # 绘制点
#             draw.ellipse((x - 0.5, y - 0.5, x + 0.5, y + 0.5), fill='white')
#     traj_path = os.path.join(traj_point_dir, f"traj_point_{idx}.png")
#
#     # 画路网线
#     if 'MultiLineString' in map.geom_type.unique():
#         map = map.explode(ignore_index=True)
#     for index, row in map.iterrows():
#         line = row['geometry']
#         # 获取线的宽度，并将其除以10
#         width_factor = int(int(row["WIDTH"]) / 10)
#
#         # 将线的坐标转换为像素坐标
#         coordinates = np.array(line.coords)
#         coordinates[:, 0] -= map.bounds.minx.min()  # 将x坐标平移至左上角
#         coordinates[:, 1] = map.bounds.maxy.max() - coordinates[:, 1]  # 将y坐标平移至左上角
#         coordinates *= np.array([width / (map.bounds.maxx.max() - map.bounds.minx.min()),
#                                  height / (map.bounds.maxy.max() - map.bounds.miny.min())])  # 缩放坐标
#         coordinates = np.round(coordinates).astype(np.int32)
#         cv2.polylines(image_blank, [coordinates], isClosed=False, color=(255,),
#                       thickness=int(width_factor), lineType=cv2.LINE_AA)  # 将厚度设置为width_factor
#         mask_path = os.path.join(mask_dir, f"mask_{idx}.png")
#         cv2.imwrite(mask_path, image_blank)
#
#     image.save(traj_path)


if __name__ == '__main__':
    sat_dir = r"C:\Users\qk516\Desktop\data3\sat"
    mask_shp_dir = r"C:\Users\qk516\Desktop\data3\mask"
    mask_dir = r"C:\Users\qk516\Desktop\data3\mask\mask_cv2"
    traj_point_shp_sir = r"C:\Users\qk516\Desktop\data3\trajectory_point"
    traj_point_dir = r"C:\Users\qk516\Desktop\data3\trajectory_point\traj_point"
    count = len([file for file in os.listdir(sat_dir) if file.endswith("tif")])
    for i in tqdm(range(count)):
        map_name = f"mask_{i}.shp"
        sat_name = f"sat_{i}.tif"
        traj_point_name = f"point_{i}.shp"
        map_path = os.path.join(mask_shp_dir, map_name)
        sat_path = os.path.join(sat_dir, sat_name)
        traj_point_path = os.path.join(traj_point_shp_sir, traj_point_name)

        image = Image.open(sat_path)
        image1 = cv2.imread(sat_path)
        traj = gpd.read_file(traj_point_path)
        map = gpd.read_file(map_path)

        if traj is None or map is None:
            continue
        xmin, ymin, xmax, ymax = traj.total_bounds
        width, height = image.size

        # 计算墨卡托投影坐标到像素坐标的转换比例
        x_range = xmax - xmin
        y_range = ymax - ymin
        x_scale = width / x_range
        y_scale = height / y_range

        height, width, _ = image1.shape
        image_blank = np.zeros((height, width), dtype=np.uint8)  # 创建一个空白图像
        image = Image.new('RGBA', (width, height), "black")
        # image.paste(map_image, (0, 0))
        draw = ImageDraw.Draw(image)

        # 画轨迹点
        # for index, row in traj.iterrows():
        #     if row.geometry.geom_type == 'Point':
        #         # 转换墨卡托投影坐标到像素坐标
        #         x = int((row.geometry.x - xmin) * x_scale)
        #         y = int((ymax - row.geometry.y) * y_scale)
        #         # 绘制点
        #         draw.ellipse((x - 0.5, y - 0.5, x + 0.5, y + 0.5), fill='white')
        # traj_path = os.path.join(traj_point_dir, f"traj_point_{i}.png")
        #
        test_mask = r"C:\Users\qk516\Desktop\data3\mask\mask_53.shp"
        test_output = r"C:\Users\qk516\Desktop\data3\mask\test\mask_53.png"

        # 画路网线
        if 'MultiLineString' in map.geom_type.unique():
            map = map.explode(ignore_index=True)
        for index, row in map.iterrows():
            line = row['geometry']
            coordinates = np.array(line.coords)
            coordinates[:, 0] -= map.bounds.minx.min()  # 将x坐标平移至左上角
            coordinates[:, 1] = map.bounds.maxy.max() - coordinates[:, 1]  # 将y坐标平移至左上角
            coordinates *= np.array([width / (map.bounds.maxx.max() - map.bounds.minx.min()),
                                     height / (map.bounds.maxy.max() - map.bounds.miny.min())])  # 缩放坐标
            coordinates = np.round(coordinates).astype(np.int32)
            cv2.polylines(image_blank, [coordinates], isClosed=False, color=(255,),
                          lineType=cv2.LINE_AA)  # 将厚度设置为width_factor
            mask_path = os.path.join(mask_dir, f"mask_{i}.png")
            cv2.imwrite(mask_path, image_blank)
