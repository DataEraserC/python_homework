import jieba
excludes = {"不知", "什么", "-----------------------", "就是", "进来", "咱们", "东西", "告诉", "回来", "只得", "只是", "大家", "这样", "不敢", "这些", "所以", "这么", "出去", "的话", "不好", "不过",
            "过来", "屋里", "心里", "一时", "不能", "今日", "没有", "只见", "听见", "两个", "这个", "不是", "那里", "这里", "一个", "一面", "如今", "说道", "知道", "我们", "你们", "他们", "怎么", "自己", "出来", "起来"}
txt = open("/home/nixos/Documents/code/python_homework/红楼梦.txt",
           "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1 or word in excludes:
        continue
    elif word in ["贾宝玉", "宝玉"]:
        rword = "贾宝玉"
    elif word in ["林黛玉", "黛玉", "林妹妹"]:
        rword = "林黛玉"
    elif word in [""]:
        rword = ""
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print("{0:<10} {1:>5}".format(word, count))
print(counts)
