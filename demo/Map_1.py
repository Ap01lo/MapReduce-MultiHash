# 获取数据
def getData(filename):
    print(f"Step 1:Reading Files from: {filename}...")
    with open(filename,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        print("Step 1:Done")
    return lines
 # 切割数据
def splitData(datalines,map_output):
    print(f"Step 2:Spliting words to output file: {map_output}...")
    with open(map_output,"w",encoding="UTF-8") as f:
        for i,line in enumerate(datalines):
            line = line.rstrip().split()
            # 输出map_output
            for item in line:
                f.write(item+"\t1\n")
            print(f"Step 2:Line {i} Done")
    print("Step 2:Done")




if __name__ == "__main__":
    filename = "data.txt"
    map_output = "map_output_1"
    datalines = getData(filename)
    splitData(datalines,map_output)