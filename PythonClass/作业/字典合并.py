# 输入用字符串表示两个字典，输出合并后的字典。字典的键用一个字母或数字表示。注意：1和‘1’是不同的关键字！

# 输入格式:
# 在第一行中输入第一个字典字符串；

# 在第二行中输入第二个字典字符串。

# 输出格式:
# 在一行中输出合并的字典，输出按字典序。

# "1" 的 ASCII 码为 49，大于 1，排序时 1 在前，"1" 在后。其它的字符同理。

# 输入样例1:
# 在这里给出一组输入。例如：

# {1:3,2:5}
# {1:5,3:7} 

# 输出样例1:
# 在这里给出相应的输出。例如：

# {1:8,2:5,3:7}

# 输入样例2:
# 在这里给出一组输入。例如：

# {"1":3,1:4}
# {"a":5,"1":6}

# 输出样例2:
# 在这里给出相应的输出。例如：

# {1:4,"1":9,"a":5}

from typing import Dict, Any
from ast import literal_eval

def sortDict(d: Dict[Any, int]) -> tuple:
    key, _ = d
    if isinstance(key, int):
        return (0, key)
    elif isinstance(key, str):
        return (1, key)
    else:
        return (2, str(key))

def unionDict(d1: Dict[Any, int], d2: Dict[Any, int]) -> Dict[Any, int]:
    res = d1.copy()
    for key, val in d2.items():
        if key in d1:
            res[key] += val
        else:
            res[key] = val
    return res

def mergeDict(d1: Dict[Any, int], d2: Dict[Any, int]) -> Dict[Any, int]:
    res = dict(d1)
    for k, v in d2.items():
        res[k] = res.get(k, 0) + v
    return res

def outputDict(d: Dict[Any, int]) -> str:
    res = []
    for k, v in d.items():
        if isinstance(k, str):
            res.append(f'"{k}":{v}')
        else:
            res.append(f'{k}:{v}')
    return "{" + ",".join(res) + "}"

def main():
    dictStr1 = input().strip()
    dictStr2 = input().strip()
    
    d1 = literal_eval(dictStr1)
    d2 = literal_eval(dictStr2)
    
    mergedDict = unionDict(d1, d2)
    
    sortedItems = sorted(mergedDict.items(), key=sortDict)
    
    print(outputDict(dict(sortedItems)))
    
    
if __name__ == "__main__":
    main()
    