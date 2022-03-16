# 从map_output读取文件
def getMapData(map_output):
    with open(map_output,encoding="UTF-8") as f:
        lines = f.readlines()
    return lines

# 整合条目
def reduce(lines,reduce_output):
    item_list = []
    item_count = []
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
            f.write(item_list[n]+"\t"+str(item_count[n])+"\n")

if __name__ == "__main__":
    map_output = "map_output_1"
    reduce_output = "reduce_output_1"
    lines = getMapData(map_output)
    reduce(lines,reduce_output)