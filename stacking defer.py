def main():
    print("counting")

    deferred = []

    for i in range(10):
        deferred.append(i)  

    print("done")

    
    for i in reversed(deferred):
        print(i)

main()




