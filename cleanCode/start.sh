#!/bin/sh

# 得到第一次mapreduce结果，并输出到 mapreducOutput_1文件中
cat ../data_0| python3 map.py | sort |python3 reduce.py | sort -k 2 > mapreduceOutput_1.txt

# 第一次扫描后续程序

## getPinFan()

cat mapreduceOutput_1.txt | python3 getPinFan.py 56 | python3 getPairs.py > pairNum.txt

## hash() && judge()
cat pairNum.txt | python3 hash.py 4 3 pairNum.txt > fakeList.txt

## map2()
cat ../data_0 | python3 map2.py fakeList.txt | sort | python3 reduce2.py | python3 getPinFanPairs.py 21
