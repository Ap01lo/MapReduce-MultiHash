# 功能：分割数据返回（item，1）

# 输入：原始数据.txt

# 输出：（item \t 1）

import sys  
# input comes from STDIN (standard input)  
for line in sys.stdin:  
    # remove leading and trailing whitespace  
    line = line.strip()  
    # split the line into words  
    words = line.split()  
    # increase counters  
    for word in words:  
        print('%s\t%s' % (word, 1))