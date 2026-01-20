def split(sum):
    x = sum * 4 // 9
    y = sum - x
    return x, y

print(split(17))
