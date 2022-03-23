import Core


def banner():
    with open("./banner.txt", "r+", encoding="UTF-8") as file:
        print(file.read())


if __name__ == "__main__":
    banner()
    Core.start()
