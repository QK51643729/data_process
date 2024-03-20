import geopandas as gpd
from shapely.geometry import Polygon
import rasterio
from rasterio.mask import mask
import matplotlib.pyplot as plt
import os

grid = "C:/Users/qk516/Desktop/data2/grid.shp"
sat = "C:/Users/qk516/Desktop/data2/fine.tif"
tra = "C:/Users/qk516/Desktop/data2/trajectory_mercator.shp"
map = "C:/Users/qk516/Desktop/data2/map_mercator.shp"
mask_path = "C:/Users/qk516/Desktop/data2/mask/"
sat_path = "C:/Users/qk516/Desktop/data2/sat/"
width_column = 'WIDTH'


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


data_grid = gpd.read_file(grid)
# data_sat = gpd.read_file(sat)
data_map = gpd.read_file(map)

for idx, boundary in data_grid.iterrows():
    left = boundary['left']
    right = boundary['right']
    top = boundary['top']
    bottom = boundary['bottom']
    # bound = Polygon([(left, bottom), (left, top), (right, bottom), (right, top)])
    clipped_mask = data_map.cx[left:right, bottom:top]

    # 裁剪mask
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    clipped_mask.apply(
        lambda x: ax.plot(x.geometry.xy[0], x.geometry.xy[1], linewidth=width_expression(x[width_column]),
                          color='white'), axis=1)
    ax.axis('off')
    plt.tight_layout()
    file_name = f"{idx}.png"
    # plt.savefig(os.path.join(mask_path, file_name), dpi=100, bbox_inches='tight', pad_inches=0, transparent=True)
    # plt.show()
    plt.close()

    # 裁剪sat
    # with rasterio.open(sat) as src:
    #     out_image, out_transform = mask(src, boundary.geometry.apply(mapping), crop=True)
    #     out_meta = src.meta.copy()
