import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 自定义数据
categories = ['语文', '数学', '英语', '物理', '化学', '生物', '地理', '历史', '政治', '体育']
data = np.array([[60, 100, 90, 40, 80, 80, 70, 40, 50, 100],
                 [100, 60, 50, 90, 90, 90, 40, 80, 80, 70],
                 [80, 90, 70, 70, 60, 90, 90, 40, 80, 80]])
name = ['学生A', '学生B', '学生C']
ave = []
for i in range(len(categories)):
    sum = 0
    for k in range(len(data)):
        sum += data[k][i]
    ave.append(sum/len(data))


# 创建一个绘图对象和子图
fig, ax = plt.subplots(figsize=(100, 100), subplot_kw=dict(polar=True))

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# 绘制每一个数据
for i, d in enumerate(data):
    values = np.concatenate((d, [d[0]]))  # 将数据首位相连，形成闭环
    ax.plot(angles, values, label=name[i])
    ax.fill(angles, values, alpha=0.1)  # 填充闭环区域

values = np.concatenate((ave, [ave[0]]))  # 将数据首位相连，形成闭环
ax.plot(angles, values, label='平均')
ax.fill(angles, values, alpha=0.1)  # 填充闭环区域


# 设置刻度标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# 添加标题和图例
ax.set_title('学生成绩雷达图')
ax.legend(loc='upper right')

# 显示图形
plt.show()
