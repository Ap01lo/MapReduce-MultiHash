import sys

# 存放频繁项
pinfanItems = []

for line in sys.stdin:

    line = line.strip()

    item = line.split()[0]
    
    pinfanItems.append(item)

# print(pinfanItems)

# 生成项对
count = 0
for itemCount1,item1 in enumerate(pinfanItems):
    for itemCount2 in range(itemCount1+1,len(pinfanItems)):
        print(str(count)+"\t"+item1+"\t"+pinfanItems[itemCount2])
        count += 1