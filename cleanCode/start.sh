#!/bin/sh

# 全局变量控制区————————————
echo "setting parameters..."
threshold_1=110
threshold_2=40

bucketSize=4
thresholdHash=3

# ——————————————————————————
echo "1st mapreducing..."
# 得到第一次mapreduce结果，并输出到 mapreducOutput_1文件中
cat ../data_0| python3 map.py | sort |python3 reduce.py | sort -k 2 > mapreduceOutput_1.txt
echo "Result with threshold ${threshold_1}:"
cat mapreduceOutput_1.txt
# 第一次扫描后续程序

## getPinFan()
echo "get PinFan items..."
cat mapreduceOutput_1.txt | python3 getPinFan.py ${threshold_1} | python3 getPairs.py > pairNum.txt

echo "Hashing..."
## hash() && judge()
cat pairNum.txt | python3 hash.py ${bucketSize} ${thresholdHash} pairNum.txt > fakeList.txt

echo "2nd mapreducing..."
## map2()
cat ../data_0 | python3 map2.py fakeList.txt | sort | python3 reduce2.py | python3 getPinFanPairs.py ${threshold_2}
