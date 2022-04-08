# 对二元伪频繁项对的计数
import sys

# 读取伪频繁项对
with open(sys.argv[1],'r') as f:
    pairs = f.readlines()

# 存放伪频繁项对
fakeList = []
for pair in pairs:
    pair = pair.strip().split()
    fakeList.append(pair)

for i,line in enumerate(sys.stdin):
    line = line.strip()
    words = line.split()

    for item in fakeList:
        if (item[0] in words) and (item[1] in words):
            print(item,"\t",1)