def biggerNum(list):
    if len(list) == 0:
        return 0
    else:
        return max(list[0], biggerNum(list[1:]))
    
print(biggerNum([1, 2, 3, 4, 5, 99999, 6, 7, 8, 9, 10]))