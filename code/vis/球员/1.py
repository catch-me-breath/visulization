import pandas as pd
from io import StringIO

# 提供的原始数据
data = """
G2,骑士,负,5,1/1,0/0,0/0,0,1,1,0,0,0,0,0,2,1
G3,骑士,胜,1,0/0,0/0,0/0,0,0,0,0,0,0,0,0,0,-2
G4,独行侠,负,5,0/2,0/1,0/0,0,1,1,0,0,0,0,0,0,7


"""

# 将数据转换为 DataFrame
df = pd.read_csv(StringIO(data), header=None)

# 格式化数据
formatted_data = []
for index, row in df.iterrows():
    game_id = f"<a href='ttt{row[0]}{row[1]}.html'>{row[0]}</a>"  # 生成带队伍名称的链接
    team = row[1]
    result = row[2]
    points = row[3]
    shooting_stats = row[4:7].tolist()  # 获取投篮统计
    additional_stats = row[7:].tolist()  # 获取其他统计数据
    formatted_row = [game_id, team, result, points] + shooting_stats + additional_stats
    formatted_data.append(formatted_row)

# 输出最终的 JavaScript 数据
formatted_js = "const data2 = " + str(formatted_data) + ";"

# 打印输出结果
print(formatted_js)
