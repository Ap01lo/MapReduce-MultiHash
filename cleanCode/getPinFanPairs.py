# 最后一步，获取二元频繁项
import sys

for line in sys.stdin:
    line = line.strip()
    
    if int(line.split()[2]) >= int(sys.argv[1]):
        print(line)