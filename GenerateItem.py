from random import randint

item_list = ["香蕉","橘子","苹果","尿布","啤酒","可乐","红茶","酸奶","绿茶","抹布"]

with open("data_0","w",encoding="UTF-8") as f:
    for i in range(100):
        for j in range(randint(4,8)):
            f.write(item_list[randint(0,9)]+"\t")
        f.write("\n")