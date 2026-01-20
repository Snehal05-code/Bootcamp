
def index(s, x):
    for i, v in enumerate(s):
        if v == x:
            return i
    return -1


def main():
    si = [10, 20, 15, -10]
    print(index(si, 15))

    ss = ["foo", "bar", "baz"]
    print(index(ss, "hello"))


main()
