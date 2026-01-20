import platform

def check_os():
    os = platform.system().lower()

    print("Go runs on ", end="")

    match os:
        case "darwin":
            print("macOS.")
        case "linux":
            print("Linux.")
        case _:
            print(f"{os}.")


def main():
    check_os()

main()

	
