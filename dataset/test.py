import shapefile
import pandas as pd

# 打开 Shapefile
# sf = shapefile.Reader("E:/轨迹数据/map/Rbeijing_polyline.shp")
#
# # 获取所有点的几何数据
# shapes = sf.shapes()
# records = sf.records()
# # shapes
# # records
#
# df = pd.DataFrame(columns=['width', 'geometry'])
# for record, shape in zip(records, shapes):
#     width = record['WIDTH']
#     geometry = shape.points
#
#     # 将数据添加到 DataFrame
#     df = df.append({'width': width, 'geometry': geometry}, ignore_index=True)
#
# df
