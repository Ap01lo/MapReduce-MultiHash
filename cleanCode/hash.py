# 两个哈希函数，分别将生成的项对哈希到两组哈希桶中，并返回位图
# 系统参数：
# argv[1]；桶大小
# argv[2]：频繁桶置信度
# argv[3]：项对编号文件路径
import sys

# 哈希子函数
def hash1(x):
    return ((x % 7) ^ 2) % int(sys.argv[1])

def hash2(x):
    return ((x + 5) % int(sys.argv[1]))

# 位图生成子函数
def bitMap(buckets,support):
    bitmap = 0
    for bucket in buckets:
        if len(bucket) >= int(support):
            # 比置信度大，置1左移
            bitmap += 1
            bitmap <<= 1 
        else:
            # 比置信度小，置0左移
            bitmap <<= 1
    bitmap >>= 1
    return bitmap

# 输出指定位二进制数（位图转换使用）
def toBin(value,num):
    binChars = ''
    temp = value
    for i in range(int(num)):
        binChar = bin(temp%2)[-1]
        temp = temp // 2
        binChars = binChar + binChars
    return binChars.upper()

# hash阶段
def hash():
    # 两个函数的哈希桶
    hashBucket1 = [[] for _ in range(int(sys.argv[1]))]
    hashBucket2 = [[] for _ in range(int(sys.argv[1]))]

    for line in sys.stdin:

        line = line.strip()
    
        # 读取项对编号
        itemNum = int(line.split()[0])

        # 哈希到桶中
        hashBucket1[hash1(itemNum)].append(itemNum)
        hashBucket2[hash2(itemNum)].append(itemNum)
    
    # 生成位图
    bitmap1 = bitMap(hashBucket1,sys.argv[2])
    bitmap2 = bitMap(hashBucket2,sys.argv[2])

    return hashBucket1,hashBucket2,bitmap1,bitmap2

# judge 阶段

def judge(hashBucket1,hashBucket2,bitmap1,bitmap2):
    # 读取项对编号文件
    with open(sys.argv[3],"r") as f:
        lines = f.readlines()
        
    bitmap1 = toBin(bitmap1,sys.argv[1])
    bitmap2 = toBin(bitmap2,sys.argv[1])


    # 伪频繁项对列表
    fakeList = []
    for line in lines:
        pairNum = int(line.split()[0])
        
        # 标记是否在频繁桶中
        flag_1 = 0
        flag_2 = 0 
        
        for i,j in enumerate(bitmap1):
            if int(j):
                if (pairNum in hashBucket1[i]):
                    flag_1 = 1
                    break

        for i,j in enumerate(bitmap2):
            if int(j):
                if (pairNum in hashBucket2[i]):
                    flag_2 = 1
                    break
        if flag_1 and flag_2:
            fakeList.append(pairNum)

    # 输出项对
    for line in lines:
        line = line.strip().split()

        if int(line[0]) in fakeList:
            print(line[1]+"\t"+line[2])


hashBucket1,hashBucket2,bitmap1,bitmap2 = hash()

judge(hashBucket1,hashBucket2,bitmap1,bitmap2)
