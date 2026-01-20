def main():
    # Test Walk
    ch = Queue()
    t = new_tree(1)

    threading.Thread(target=lambda: Walk(t, ch)).start()

    print("Walk output:")
    for _ in range(10):
        print(ch.get(), end=" ")

    print("\n")

    # Test Same
    print("Same(tree.New(1), tree.New(1)) →",
          Same(new_tree(1), new_tree(1)))

    print("Same(tree.New(1), tree.New(2)) →",
          Same(new_tree(1), new_tree(2)))


if __name__ == "__main__":
    main()
