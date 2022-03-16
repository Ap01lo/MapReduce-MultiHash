# -*- coding: UTF-8 -*-
# 产生两两项对
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 获取数据
from fileinput import filename


def getData(filename):
    print(f"Step 1:Reading Files from: {filename}...")
    with open(filename,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        print("Step 1:Done")
    return lines


def generatePairs(lines):
    item_list = []
    pair_list = []
    for line in lines:
        item = line.rstrip().split()[0]
        item_list.append(item)
    # 产生项对
    for i in range(len(item_list)-1):
        for j in range(len(item_list)-1-i):
            pair_list.append((item_list[i],item_list[i+j+1])) 
    # 存储到文档里面
    with open("Pairs_1","w",encoding="UTF-8") as f:
        for i,item in enumerate(pair_list):
            f.write(str(i)+"\t"+item[0]+"\t"+item[1]+"\n")
    
    return item_list
if __name__ == "__main__":
    filename = "reduce_output_1"
    datalines = getData(filename)
    generatePairs(datalines) 