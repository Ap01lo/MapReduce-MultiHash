# 最终频繁项计数
import io
import sys

# 二元频繁项阈值
# THRESHOLD = 2050

from cv2 import line, split
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
   
def Count(pairs_list,pair_0,data_0,reduce_output_0,THRESHOLD):
    # item_list 存储物品种类，从reduce_output_0读取
    item_list = [] # 物品种类
    with open(reduce_output_0,"r",encoding="UTF-8") as f:
        lines = f.readlines()
    for item in lines:
        item_list.append(item.split()[1])

    # 将pairs_list转化为数字项对
    pairs_num = []
    with open(pair_0,"r") as f:
        lines = f.readlines()
    for i in pairs_list:
        for c,line in enumerate(lines):
            if i == c:
                line = line.split()
                pairs_num.append((int(line[1]),int(line[2])))
    # count_list 存储伪二元频繁项的计数
    count_list = [0 for i in range(len(pairs_list))]

    with open(data_0,"r",encoding="UTF-8") as f: 
       lines = f.readlines()
    for t,pair in enumerate(pairs_num):# 伪项对
        for item in lines:# 源数据行
            if item_list[pair[0]] in item.split() and item_list[pair[1]] in item.split():
                count_list[t] += 1
    
    print(count_list) 
    print(f"The Threshold of 2 items is {THRESHOLD} of {len(count_list)}")
    # 得到了伪频繁项对的计数，根据阈值筛选二元频繁项
    pair_pf = []
    for c,i in enumerate(count_list):
        if i >= THRESHOLD:
            pair_pf.append((item_list[pairs_num[c][0]],item_list[pairs_num[c][1]]))
    return pair_pf

if __name__ == "__main__":
    pairs_list = [17, 18, 24, 28, 33]
    Count(pairs_list,"Pairs_0","data_0","reduce_output_0")