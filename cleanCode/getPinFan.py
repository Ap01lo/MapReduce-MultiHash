import sys

for line in sys.stdin:

    # 去掉行尾换行符
    line = line.strip()

    # 拆分行，变为(item,n)格式
    words = line.split("\t")

    # 判断是否大于一元频繁项阈值，是的话输出该元素
    if int(words[1]) > int(sys.argv[1]):
        print(f"{words[0]}\t{words[1]}")