def toBin(value,num):
    binChars = ''
    temp = value
    for i in range(num):
        binChar = bin(temp%2)[-1]
        temp = temp // 2
        binChars = binChar + binChars
    return binChars.upper()


a = 5
print(toBin(a,8))