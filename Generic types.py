# List represents a singly linked list that holds any type
class List:
    def __init__(self, val):
        self.val = val
        self.next = None


def main():
    # Creating linked list nodes
    n1 = List(10)
    n2 = List(20)
    n3 = List(30)

    # linking nodes
    n1.next = n2
    n2.next = n3

    # print the list
    current = n1
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


main()
