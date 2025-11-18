class Person:
# 成员变量
    __name: str
    __age: int
    __chinese: float
    __math: float
    __english: float

# 构造函数
    def __init__(self, name: str, age: int, chinese: float, math: float, english: float) -> None:
        self.__name = name
        self.__age = age
        self.__chinese = chinese
        self.__math = math
        self.__english = english

# 其他方法
    def setName(self, name: str) -> None:  # 设置姓名
        self.__name = name

    def getName(self) -> str:   # 获取姓名
        return self.__name
    
    def setAge(self, age: int) -> None:    # 设置年龄
        self.__age = age
        
    def getAge(self) -> int:    # 获取年龄
        return self.__age

    def setChinese(self, chinese: float) -> None:  # 设置成绩
        self.__chinese = chinese
        
    def setMath(self, math: float) -> None:
        self.__math = math
        
    def setEnglish(self, english: float) -> None:
        self.__english = english
        
    def getScores(self) -> tuple:   # 获取成绩
        return (self.__chinese, self.__math, self.__english)

    def totalScore(self) -> float:   # 计算总分
        return self.__chinese + self.__math + self.__english

    def averageScore(self) -> float:    # 计算平均分
        return self.totalScore() / 3

    def isAdult(self) -> bool:    # 判断是否成年
        return self.__age >= 18
    
    def isPassed(self) -> bool:   # 判断是否及格
        return self.__chinese >= 60 and self.__math >= 60 and self.__english >= 60


if __name__ == "__main__":
    p = Person("Caesar", 18, 90, 80, 85)
    print(p)