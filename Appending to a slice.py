def print_slice(s):
    print(f"len={len(s)} {s}")

def main():
    s = []
    print_slice(s)

    # append works on empty list
    s.append(0)
    print_slice(s)

    # list grows as needed
    s.append(1)
    print_slice(s)

    # add more than one element
    s.extend([2, 3, 4])
    print_slice(s)

main()

