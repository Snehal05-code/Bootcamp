def main():

    pow = [0] * 10

    
    for i in range(len(pow)):
        pow[i] = 1 << i      

    
    for value in pow:
        print(value)

main()
