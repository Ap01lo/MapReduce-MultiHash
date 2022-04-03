# 频繁项置信度
# ITEM_SUPPORT = 6000

# 从map_output读取文件
def getMapData(map_output):
    with open(map_output,encoding="UTF-8") as f:
        lines = f.readlines()
    return lines

# 整合条目
def reduce(lines,reduce_output,item_pf_output,ITEM_SUPPORT):
    item_list = []
    item_count = []
    item_pf = []
    for line in lines:
        if line.split()[0] not in item_list:
            item_list.append(line.split()[0])
            item_count.append(1)
        else:
            i = item_list.index(line.split()[0])
            item_count[i] += 1
    # 输出reduce_output
    with open(reduce_output,"w",encoding="UTF-8") as f:
        for n in range(len(item_list)):
            f.write(str(n)+"\t"+item_list[n]+"\t"+str(item_count[n])+"\n")
            if item_count[n] >= ITEM_SUPPORT:
                item_pf.append(n)
    # 输出单元素频繁项
    with open(item_pf_output,"w") as f:
        for item in item_pf:
            f.write(str(item)+"\n")
    print(f"The Threshold of 1 pf is {ITEM_SUPPORT} of {len(item_pf)}")
    return item_pf
                
                
if __name__ == "__main__":
    map_output = "map_output_1"
    reduce_output = "reduce_output_1"
    item_pf_output = "item_pf_output_1"
    lines = getMapData(map_output)
    reduce(lines,reduce_output,item_pf_output)