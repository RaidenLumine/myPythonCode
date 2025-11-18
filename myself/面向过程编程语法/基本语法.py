"""
    锄禾日当午
    汗滴禾下土
    水煮盘中餐
    粒粒皆辛苦
"""

def string1():
    name = """
        锄禾日当午
        汗滴禾下土
        水煮盘中餐
        粒粒皆辛苦
    """
    print(name)
    
def string2():
    t1 = "Caesar"
    t2 = "male"
    t3 = 440606
    print("My name is "+t1+". I'm a "+t2+". My ID is "+str(t3))
    
def string3():
    t1 = "Caesar"
    t2 = "male"
    t3 = 440606
    print("My name is %s. I'm a %s. My ID is %.0f" % (t1,t2,t3))
    
def cmp():
    print('abd' > 'abc')
    print('c' > 'ab')
    print('abc' > 'ab')
    print('abc' > 'ad')

def main():
    #string1()
    #string2()
    #string3()
    cmp()
    
if __name__ == "__main__":
    main()