# 全局变量
HASH_SUPPORT = 6
BUCKET_SIZE = 8

# 第一个哈希函数
def hash_1(pair2num,bucket_size):    
    bucket = [[] for i in range(bucket_size)]
    for item in pair2num:
        hash_value = item%bucket_size
        bucket[hash_value].append(item)
    bitmap =generate_bitmap(bucket,HASH_SUPPORT)
    return bitmap,bucket

# 第二个哈希函数
def hash_2(pair2num,bucket_size):
    bucket = [[] for i in range(bucket_size)]
    for item in pair2num:
        hash_value = (item+5)%bucket_size
        bucket[hash_value].append(item)
    bitmap = generate_bitmap(bucket,HASH_SUPPORT)
    return bitmap,bucket


def get_pairs(filename):
    pair2num = []
    with open(filename,"r") as f:
        lines = f.readlines()
    for line in lines:
        pair2num.append(int(line.split()[0]))
    return pair2num

# 产生位图
def generate_bitmap(buckets,support):
    bitmap = 0
    for bucket in buckets:
        if len(bucket) >= support:
            # 比置信度大，置1左移
            bitmap += 1
            bitmap <<= 1 
        else:
            # 比置信度小，置0左移
            bitmap <<= 1
    bitmap >>= 1
    return bitmap

if __name__ == "__main__":
    filename = "Pairs_1"
    pair2num = get_pairs(filename)
    bitmap_1 = hash_1(pair2num,BUCKET_SIZE)
    bitmap_2 = hash_2(pair2num,BUCKET_SIZE)