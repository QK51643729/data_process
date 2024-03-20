import pandas as pd

# 读取数据
with open("D:/data/beijing-taxi-l.txt", 'r') as file:
    lines = file.readlines()

# 解析数据
trajectory_data = []
for line in lines:
    parts = line.strip().split('|')
    trajectory_id = int(parts[0])
    points_data = parts[1].split(',')
    points = [point.split() for point in points_data]
    trajectory_data.append({'TrajectoryID': trajectory_id, 'Points': points})

# 转为DataFrame
df = pd.DataFrame(trajectory_data)

# 展开轨迹点数据
expanded_data = df.explode('Points')

# 拆分 Points 列为 Longitude、Latitude、Timestamp、Value1、Value2 列
expanded_data[['Longitude', 'Latitude', 'Timestamp', 'Speed', 'Direct']] = pd.DataFrame(
    expanded_data['Points'].tolist(), index=expanded_data.index)

# 删除不再需要的列
expanded_data.drop(columns=['Points'], inplace=True)

# 将相关列转为数值类型
expanded_data[['Longitude', 'Latitude', 'Timestamp', 'Speed', 'Direct']] = expanded_data[
    ['Longitude', 'Latitude', 'Timestamp', 'Speed', 'Direct']].apply(pd.to_numeric)

# 预览处理后的数据
print("处理后的数据:")
print(expanded_data)

# 保存为CSV
expanded_data.to_csv("D:/data/beijing-taxi-l.csv", index=False)
