import os

import cv2
import geopandas as gpd
from shapely.geometry import MultiLineString
import numpy as np
from tqdm import tqdm


# image = cv2.imread(r"C:\Users\qk516\Desktop\data3\sat\sat_0.tif")
# gdf = gpd.read_file(r"C:\Users\qk516\Desktop\data3\mask\mask_0.shp")


def draw_mask(idx):
    map_name = f"mask_{idx}.shp"
    sat_name = f"sat_{idx}.tif"
    traj_point_name = f"point_{idx}.shp"
    map_path = os.path.join(mask_shp_dir, map_name)
    sat_path = os.path.join(sat_dir, sat_name)
    traj_point_path = os.path.join(traj_point_dir, traj_point_name)

    gdf = gpd.read_file(map_path)
    image = cv2.imread(sat_path)
    traj = gpd.read_file(traj_point_path)

    height, width, _ = image.shape
    image_blank = np.zeros((height, width), dtype=np.uint8)  # 创建一个空白图像

    if gdf.empty:
        # print(f"{idx}为空！")
        mask_path = os.path.join(mask_dir, f"mask_{idx}.png")
        cv2.imwrite(mask_path, image_blank)

    if 'MultiLineString' in gdf.geom_type.unique():
        gdf = gdf.explode(ignore_index=True)
    for index, row in gdf.iterrows():
        line = row['geometry']
        # 获取线的宽度，并将其除以10
        width_factor = int(int(row["WIDTH"]) / 10)

        # 将线的坐标转换为像素坐标
        coordinates = np.array(line.coords)
        coordinates[:, 0] -= gdf.bounds.minx.min()  # 将x坐标平移至左上角
        coordinates[:, 1] = gdf.bounds.maxy.max() - coordinates[:, 1]  # 将y坐标平移至左上角
        coordinates *= np.array([width / (gdf.bounds.maxx.max() - gdf.bounds.minx.min()),
                                 height / (gdf.bounds.maxy.max() - gdf.bounds.miny.min())])  # 缩放坐标

        # 将坐标转换为整数
        coordinates = np.round(coordinates).astype(np.int32)

        # 在图像上绘制线
        cv2.polylines(image_blank, [coordinates], isClosed=False, color=(255,),
                      thickness=int(width_factor), lineType=cv2.LINE_AA)  # 将厚度设置为width_factor
        mask_path = os.path.join(mask_dir, f"mask_{idx}.png")
        cv2.imwrite(mask_path, image_blank)

    # cv2.imshow("Shapefile Visualization", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    sat_dir = r"C:\Users\qk516\Desktop\data3\sat"
    mask_shp_dir = r"C:\Users\qk516\Desktop\data3\mask"
    mask_dir = r"C:\Users\qk516\Desktop\data3\mask\mask_cv2"
    traj_point_shp_sir = r"C:\Users\qk516\Desktop\data3\trajectory_point"
    traj_point_dir = r"C:\Users\qk516\Desktop\data3\trajectory_point\traj_point"
    count = len([file for file in os.listdir(sat_dir) if file.endswith("tif")])
    for i in tqdm(range(count)):
        draw_mask(i)
