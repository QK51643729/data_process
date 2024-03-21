# -*- coding: utf-8 -*-
"""
@author: kqiao
@date: 2024/3/20
"""

import os
import random
import shutil

sat_dir = r"C:\Users\qk516\Desktop\data3\sat"
mask_dir = r"C:\Users\qk516\Desktop\data3\mask\mask_cv2"
traj_dir = r"C:\Users\qk516\Desktop\data3\trajectory_point\traj_point"
test_sat_dir = r"C:\Users\qk516\Desktop\data3\test\image"
test_mask_dir = r"C:\Users\qk516\Desktop\data3\test\mask"
test_gps_dir = r"C:\Users\qk516\Desktop\data3\test\gps"
train_sat_dir = r"C:\Users\qk516\Desktop\data3\train\image"
train_mask_dir = r"C:\Users\qk516\Desktop\data3\train\mask"
train_gps_dir = r"C:\Users\qk516\Desktop\data3\train\gps"

split_ratio = 0.8  # 训练集比例，测试集比例为 1 - split_ratio

list = [sat_dir, mask_dir, traj_dir]
test_dir = [test_sat_dir, test_mask_dir, test_gps_dir]
train_dir = [train_sat_dir, train_mask_dir, train_gps_dir]
for index, file_dir in enumerate(list):
    files = [file for file in os.listdir(file_dir) if file.endswith('tif') or file.endswith('png')]
    random.shuffle(files)
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    test_files = files[split_index:]
    for file in train_files:
        src = os.path.join(file_dir, file)
        dst = os.path.join(train_dir[index], file)
        shutil.copy(dst, src)
    for file in test_files:
        src = os.path.join(file_dir, file)
        dst = os.path.join(test_dir[index], file)
        shutil.copy(dst, src)

print("数据集分割完成！")
