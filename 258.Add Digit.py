def addDigit(num:int):
    while num>10:
        num=sum(int(digit) for digit in str(num))
    return num
print(addDigit(38))
