def main():
    deferred = []

    deferred.append("world")

    print("hello")

    for s in reversed(deferred):
        print(s)

main()
