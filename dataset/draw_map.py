import os
import geopandas as gpd
import matplotlib

from matplotlib import pyplot as plt
from tqdm import tqdm


def width_expression(width_value):
    # Custom width expression
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


def draw(mask_path):
    mask = gpd.read_file(mask_path)
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    mask.plot(ax=ax, linewidth=mask['WIDTH'].apply(width_expression), color='white', cmap='gray')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.tight_layout()
    name = photo_file.replace(".shp", ".png")
    plt.savefig(f"C:/Users/qk516/Desktop/data3/mask/mask/{name}", dpi=100)
    plt.close()


if __name__ == '__main__':
    mask_path = "C:/Users/qk516/Desktop/data3/mask/"
    for photo_file in tqdm(os.listdir(mask_path)):
        if photo_file.endswith(".shp"):
            path = os.path.join(mask_path, photo_file)
            draw(path)
