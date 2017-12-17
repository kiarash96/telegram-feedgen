import re


def add_channel(username):
    pass


def main():
    while True:
        command = input(">> ")
        if command == "exit":
            break
        else:
            result = re.match(r"^join\s+@?(\w+)", command)
            if result:
                username = result.group(1)
                add_channel(username)


if __name__ == "__main__":
    main()
