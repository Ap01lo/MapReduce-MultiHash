def getNum(item_pf,pairnum):
    item2num_list = []
    with open(pairnum,"r") as f:
        lines = f.readlines()

    for i in item_pf:
        for j,pair in enumerate(lines):
            pair = pair.split()
            # print(i[0],pair[1],i[1],pair[2])
            if int(i[0])>j:
                continue
            if i[0] == pair[1] and i[1] == pair[2]:
                item2num_list.append(j)
    return item2num_list

def judge(item_list,bitmap_1,bitmap_2,bucket_1,bucket_2):
    pairs_pf = []

    for item in item_list:      
        flag_1 = 0 # 是否在桶1的频繁桶中
        flag_2 = 0 # 是否在桶2的频繁桶中
        for i,k in enumerate(bin(bitmap_1)[2:]):
            if int(k) :
                if (item in bucket_1[i]):
                    # print(i,k)
                    flag_1 = 1
                    break
        
        for a,b in enumerate(bin(bitmap_2)[2:]):
            if int(b) :
                if (item in bucket_2[a]):
                   #  print(k)
                    flag_2 = 1
                    break

        if flag_1 and flag_2:
            pairs_pf.append(item)
    return pairs_pf
        
if __name__ == "__main__":
    item_pf = [('2', '3'), ('2', '4'), ('2', '8'), ('3', '4'), ('3', '8'), ('4', '8')]
    ls = getNum(item_pf,"Pairs_0")
    print(ls)