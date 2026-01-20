def main():
    # make(map[string]int) → empty dictionary
    m = {}

    # assign value
    m["Answer"] = 42
    print("The value:", m["Answer"])

    # update value
    m["Answer"] = 48
    print("The value:", m["Answer"])

    # delete key
    del m["Answer"]

    # access after delete (safe way like v, ok in Go)
    v = m.get("Answer")
    ok = "Answer" in m
    print("The value:", v, "Present?", ok)

main()
