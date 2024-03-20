import os
from PIL import Image


def count_specific_size_images(directory, width, height):
    # 初始化计数器
    count = 0

    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # 检查文件是否是tif图片
        if filepath.endswith('.tif') or filepath.endswith('.tiff') or filepath.endswith('png'):
            # 打开图片
            img = Image.open(filepath)
            # 检查图片尺寸是否符合要求
            if img.width == width and img.height == height:
                count += 1
            # 关闭图片
            img.close()

    return count


# 目录路径
directory_path = 'C:/Users/qk516/Desktop/data3/view/map_line_sat/'

# 统计指定大小的图片数量
specific_size_count = count_specific_size_images(directory_path, 799, 799)
a = count_specific_size_images(directory_path, 800, 799)
b = count_specific_size_images(directory_path, 799, 800)
c = count_specific_size_images(directory_path, 800, 800)
# 输出结果
print(f"目录 {directory_path} 下尺寸为799*799的tif图片数量为: {specific_size_count}")
print(f"目录 {directory_path} 下尺寸为800*799的tif图片数量为: {a}")
print(f"目录 {directory_path} 下尺寸为799*800的tif图片数量为: {b}")
print(f"目录 {directory_path} 下尺寸为800*800的tif图片数量为: {c}")
