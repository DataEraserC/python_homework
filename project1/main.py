import jieba
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import os

#覆盖图像函数
def overlay_transparent(background_img, overlay_img):
   # 打开原始图片和透明图片
   background = background_img
   overlay = overlay_img

   # 将透明图片转换为RGBA模式
   overlay = overlay.convert('RGBA')

   # 创建一个新的图片，将原始图片和透明图片合并
   composite = Image.new('RGBA', background.size, (0, 0, 0, 0))
   composite.paste(background, (0, 0))
   composite.paste(overlay, (0, 0), mask=overlay)

   return composite

# 排除词
excludes = {"不知", "什么", "-----------------------", "就是", "进来", "咱们", "东西", "告诉", "回来", "只得",
            "只是", "大家", "这样", "不敢", "这些", "所以", "这么", "出去", "的话", "不好", "不过", "过来", "屋里",
            "心里", "一时", "不能", "今日", "没有", "只见", "听见", "两个", "这个", "不是", "那里", "这里", "一个",
            "一面", "如今", "说道", "知道", "我们", "你们", "他们", "怎么", "自己", "出来", "起来"}

#打开要统计的文件
txt = open("红楼梦.txt", "r", encoding='utf-8').read()

#精准分词
words = jieba.lcut(txt)

#初始化counts键值对
counts = {}

#合并部分关键词
for word in words:
    if len(word) == 1 or word in excludes:
        continue
    elif word in ["贾宝玉", "宝玉"]:
        rword = "贾宝玉"
    elif word in ["林黛玉", "黛玉", "林妹妹"]:
        rword = "林黛玉"
    elif word == "":
        rword = ""
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

#键值对转元组并转为列表
items = list(counts.items())
#排序
items.sort(key=lambda x: x[1], reverse=True)
#提取前20个关键词
top_20_items = items[:20]  # Get top 20 items

#打开背景图
background_image = Image.open("红楼梦.jpg")

#背景转为数组
bg_pic = np.array(background_image)

#生成词云
wordcloud = WordCloud(font_path="SimHei.ttf",
                      background_color="rgba(255, 255, 255, 0)", mode="RGBA",
                      width=800,
                      height=600,
                      mask=bg_pic).generate_from_frequencies(dict(top_20_items))

#检查输出文件夹是否存在 不存在则创建
if not os.path.exists("out"):
    os.makedirs("out")

#保存背景图片形状但无背景的词云图片
wordcloud.to_file("out/result_with_background_shape.png")
#将背景和词云依次覆盖到新生成的空白图片上
result_with_background = overlay_transparent(background_image,Image.open("out/result_with_background_shape.png"))
#保存有背景词云图片
result_with_background.save("out/result_with_background.png")
#展示图片
plt.figure(figsize=(10, 8))
plt.imshow(result_with_background, interpolation="bilinear")
plt.axis("off")
plt.show()