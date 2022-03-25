import Map_1
import Reduce_1
import Mix
import Hash
import Judge
import Count

def main():
    item_pf,bitmap_1,bitmap_2,bucket_1,bucket_2 = Scan_1()
    Scan_2(item_pf,bitmap_1,bitmap_2,bucket_1,bucket_2)

def Scan_1():
    # Map
    Map_1.MapData(Map_1.getData("data_0"),"map_output_0")

    # Reduce
    item_pf = Reduce_1.reduce(Reduce_1.getMapData("map_output_0"),"reduce_output_0","item_pf_output_0")

    # pairs2num
    Mix.generatePairs(Mix.getData("reduce_output_0"),"Pairs_0")

    # hash1
    bitmap_1,bucket_1 = Hash.hash_1(Hash.get_pairs("Pairs_0"),8)

    # hash2
    bitmap_2,bucket_2 = Hash.hash_2(Hash.get_pairs("Pairs_0"),8)


    return item_pf,bitmap_1,bitmap_2,bucket_1,bucket_2

def Scan_2(item_pf,bitmap_1,bitmap_2,bucket_1,bucket_2):

    # generate pairs with item_pf
    pairs_pre_list = Mix.generatePairs(Mix.getData("item_pf_output_0"),"Pairs_1")

    # judge if in pf_hash for each pair
    item_list = Judge.getNum(pairs_pre_list,"Pairs_0")
    pairs_list = Judge.judge(item_list,bitmap_1,bitmap_2,bucket_1,bucket_2)

    # count pair_pf
    pair_pf = Count.Count(pairs_list,"Pairs_0","data_0","reduce_output_0")
    print(pair_pf)
if __name__ == "__main__":
    main()

