# -*- coding: UTF-8 -*-
# 产生两两项对
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 获取数据
from fileinput import filename

def getData(filename):
    with open(filename,'r',encoding='UTF-8') as f:
        lines = f.readlines()
    return lines


def generatePairs(lines,pairfile):
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
    # 第一列是整数序号，用来hash
    # 第二第三列是项对
    with open(pairfile,"w",encoding="UTF-8") as f:
        for i,item in enumerate(pair_list):
            f.write(str(i)+"\t"+item[0]+"\t"+item[1]+"\n")
    return pair_list

if __name__ == "__main__":
    filename = "reduce_output_1"
    pairfile = "Pairs_0"
    datalines = getData(filename)
    generatePairs(datalines,pairfile) 