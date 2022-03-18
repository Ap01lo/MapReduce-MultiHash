# 获取数据
def getData(filename):
    with open(filename,'r',encoding='UTF-8') as f:
        lines = f.readlines()
    return lines

 # 切割数据
def MapData(datalines,map_output):
    with open(map_output,"w",encoding="UTF-8") as f:
        for i,line in enumerate(datalines):
            line = line.rstrip().split()
            # 输出map_output
            for item in line:
                f.write(item+"\t1\n")

if __name__ == "__main__":
    filename = "data_0"
    map_output = "map_output_1"
    datalines = getData(filename)
    MapData(datalines,map_output)