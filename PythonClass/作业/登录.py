def isPass(name: str, password: str) -> bool:
    dic = {
        'admin':'123456',
        'administrator':'12345678',
        'root':'password'
    }
    return password == dic.get(name)

if __name__ == '__main__':
    count = 1
    while count <= 3:
        name = input()
        password = input()
        if isPass(name, password):
            print("登录成功")
            break
        else:
            print("登录失败")
        count += 1