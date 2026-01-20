def main():
    i = [42]      
    j = [2701]

    p = i         
    print(p[0])   

    p[0] = 21     
    print(i[0])   

    p = j         
    p[0] = p[0] // 37   
    print(j[0])  


main()
