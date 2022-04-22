import Impact

name = "Impact"
input_message = f"[{name} #]"


def assets_help():
    print("----------------------Impact----------------------")
    print("1、一句话脚本连接")
    print("输入exit退出脚本")
    print("-----------------------END------------------------")


def start():
    assets_help()

    while True:
        option = input(input_message)
        if option == 'exit':
            break
        elif option == '1':
            Impact.SimpleHorse.start()
        else:
            print("无效的输入,请重新输入\n")
            assets_help()
