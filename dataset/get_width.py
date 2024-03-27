# -*- coding: utf-8 -*-
"""
@author: kqiao
@date: 2024/3/27
"""
import cv2
import numpy as np

test_sat = r"C:\Users\qk516\Desktop\data3\sat\sat_53.tif"
test_mask = r"C:\Users\qk516\Desktop\data3\mask\mask_cv2\mask_53.png"

road_centerline = np.array()


# 估计道路宽度的函数
def estimate_road_width(centerline, image):
    # 设置测量线长度
    measure_length = 20  # 可根据实际情况调整

    # 创建一个空白图像，用于绘制道路宽度
    road_width_image = np.zeros_like(image)

    # 对于每个中心线点
    for point in centerline:
        x, y = point

        # 计算中心线点的法向量，这里简单地使用 (-y, x)，可以根据实际情况调整
        normal_vector = np.array([-y, x])

        # 将法向量归一化
        normal_vector = normal_vector / np.linalg.norm(normal_vector)

        # 计算测量线的两个端点
        endpoint1 = (x - measure_length * normal_vector[0], y - measure_length * normal_vector[1])
        endpoint2 = (x + measure_length * normal_vector[0], y + measure_length * normal_vector[1])

        # 在空白图像上绘制测量线
        cv2.line(road_width_image, (int(endpoint1[0]), int(endpoint1[1])), (int(endpoint2[0]), int(endpoint2[1])),
                 (255, 255, 255), 2)

    return road_width_image


# 加载卫星图像，这里假设为一个RGB图像
# 这里的数据是假设的示例数据，实际应该从数据源中加载
satellite_image = cv2.imread('satellite_image.jpg')

# 估计道路宽度
road_width_image = estimate_road_width(road_centerline, satellite_image)

# 将道路宽度图像与卫星图像叠加
result_image = cv2.addWeighted(satellite_image, 0.7, road_width_image, 0.3, 0)

# 显示结果
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
