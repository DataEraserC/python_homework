import jieba
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import os

excludes = {"不知", "什么", "-----------------------", "就是", "进来", "咱们", "东西", "告诉", "回来", "只得",
            "只是", "大家", "这样", "不敢", "这些", "所以", "这么", "出去", "的话", "不好", "不过", "过来", "屋里",
            "心里", "一时", "不能", "今日", "没有", "只见", "听见", "两个", "这个", "不是", "那里", "这里", "一个",
            "一面", "如今", "说道", "知道", "我们", "你们", "他们", "怎么", "自己", "出来", "起来"}

txt = open("红楼梦.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}

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

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
top_20_items = items[:20]  # Get top 20 items

im = Image.open("红楼梦.jpg")
bg_pic = np.array(im)

wordcloud = WordCloud(font_path="SimHei.ttf",
                      background_color="white",
                      width=800,
                      height=600,
                      mask=bg_pic).generate_from_frequencies(dict(top_20_items))

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
if not os.path.exists("out"):
    os.makedirs("out")
wordcloud.to_file("out/result.png")
