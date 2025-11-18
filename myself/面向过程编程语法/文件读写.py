
def write1():
    # 写入
    f = open("test.txt", "a", encoding="UTF-8")
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")
    f.close()

def read1():
    # 读取文件内容
    f = open("test.txt", "r", encoding="UTF-8")
    content = f.read()
    f.close()
    print("文件内容: ", content)

def append1():
    # 追加
    f = open("test.txt","a",encoding = "UTF-8")
    f.write("我是你爹!\n")
    f.close()

def read2():
    # 读取文件内容
    f = open("test.txt", "r", encoding="UTF-8")
    document = f.read().strip()
    f.close()
    print("追加后内容：",document)