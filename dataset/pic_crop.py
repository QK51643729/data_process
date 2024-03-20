from PIL import Image
import os


def crop_and_save(image_path, output_folder, min_x, min_y, max_x, max_y, crop_size=(512, 512)):
    # 打开原始图片
    original_image = Image.open(image_path)

    # 获取原始图片的宽度和高度
    width, height = original_image.size

    # 计算裁剪后图片的行数和列数
    rows = height // crop_size[1]
    cols = width // crop_size[0]

    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 循环裁剪并保存图片
    for row in range(rows):
        for col in range(cols):
            # 计算裁剪区域的坐标
            left = col * crop_size[0]
            top = row * crop_size[1]
            right = left + crop_size[0]
            bottom = top + crop_size[1]

            # 计算经纬度
            left_bottom_x = min_x + left * (max_x - min_x) / width
            left_bottom_y = max_y - bottom * (max_y - min_y) / height
            right_top_x = min_x + right * (max_x - min_x) / width
            right_top_y = max_y - top * (max_y - min_y) / height

            # 裁剪图片
            cropped_image = original_image.crop((left, top, right, bottom))

            # 构建保存路径
            save_path = os.path.join(output_folder, f"{left_bottom_x}_{left_bottom_y}_{right_top_x}_{right_top_y}.jpg")

            # 保存裁剪后的图片
            cropped_image.save(save_path)
            print(left_bottom_x, left_bottom_y, right_top_x, right_top_y)

    print("裁剪并保存完成！")


# 输入和输出路径
input_image_path = "C:/Users/qk516/Desktop/testdata/row/test3.jpg"
output_folder_path = "C:/Users/qk516/Desktop/testdata/clipped/"
min_x, min_y, max_x, max_y = 116.3481633047014, 39.90556148060156, 116.4305553503617, 39.93625032798411

# 调用函数进行裁剪和保存
crop_and_save(input_image_path, output_folder_path, min_x, min_y, max_x, max_y, crop_size=(512, 512))
