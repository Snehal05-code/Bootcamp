
Big = 1 << 100
Small = Big >> 99  


def need_int(x):
    return x * 10 + 1

def need_float(x):
    return x * 0.1


def main():
    print(need_int(Small))
    print(need_float(Small))
    print(need_float(Big))

main()
