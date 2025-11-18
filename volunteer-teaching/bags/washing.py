import pandas as pd
def washing():
    data = {
        "姓名": ["张三", "李四", "王五", "李四", "赵六"], # 数据重复
        "零食": ["薯片", "糖果", "坚果", "巧克力", "冰淇淋 "], 
        "评分": [5, 5, None, 4, 2]
    }
    df = pd.DataFrame(data)
    
    print("----- 原始数据 -----")
    print(df)
    print(f"原始数据行数: {len(df)}")

    # 清洗方法
    # 1. 先去除字符串空格
    df_cleaned = df.copy()
    df_cleaned["姓名"] = df_cleaned["姓名"].str.strip()
    df_cleaned["零食"] = df_cleaned["零食"].str.strip()
    
    # 2. 智能去重：优先保留有完整数据的记录
    duplicates = df_cleaned[df_cleaned.duplicated(subset=['姓名'], keep=False)]
    if not duplicates.empty:
        print("发现重复记录：")
        print(duplicates)
        
        # 对于重复记录，优先保留评分不为空的记录
        # 先按姓名分组，然后在每组中优先保留非空评分的记录
        df_cleaned = df_cleaned.sort_values('评分', na_position='last')  # 将空值排到最后
        df_cleaned = df_cleaned.drop_duplicates(subset=['姓名'], keep='first')
    
    print(f"基于姓名和零食去重后行数: {len(df_cleaned)}")
    
    # 3. 处理缺失值
    df_cleaned["姓名"] = df_cleaned["姓名"].fillna("未知")  # 对评分列填充缺失值
    df_cleaned["零食"] = df_cleaned["零食"].fillna("未知")  # 对评分列填充缺失值
    df_cleaned["评分"] = df_cleaned["评分"].fillna("未知")  # 对评分列填充缺失值
    
    print("\n----- 最终数据清洗结果 -----")
    print(df_cleaned)
    print(f"最终数据行数: {len(df_cleaned)}")
    
    # 显示被删除的记录
    print("\n----- 清洗统计 -----")
    print(f" 原始数据: {len(df)} 行")
    print(f" 清洗后数据: {len(df_cleaned)} 行")
    print(f" 删除了 {len(df) - len(df_cleaned)} 行重复数据")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    washing()