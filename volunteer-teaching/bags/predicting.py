import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
def predict():
    print("\n" + "="*50)
    print(" 机器学习预测分析")
    print("="*50)
    
    # 数据
    temp = [18, 22, 25, 28, 30]  # 温度
    sales = [25, 30, 50, 60, 100]  # 销量
    # sales = sales[::-1]  # 反转销量数据，模拟销量随温度升高而增加的趋势

    x = np.array(temp).reshape(-1, 1)
    y = np.array(sales)
    model = LinearRegression().fit(x, y)

    # 预测28度时的销量
    predicted_sales = int(model.predict([[28]])[0])
    print(f" 预测28℃时的销量：{predicted_sales}个")

    # 创建预测线图
    plt.figure(figsize=(12, 7))
    plt.scatter(temp, sales, color='red', s=120, alpha=0.8, label='实际数据点', edgecolors='black')

    # 绘制预测线
    temp_line = np.linspace(min(temp)-2, max(temp)+2, 100)
    sales_line = model.predict(temp_line.reshape(-1, 1))
    plt.plot(temp_line, sales_line, color='blue', linewidth=2, label='预测趋势线', alpha=0.7)

    # 标记28度的预测点
    plt.scatter([28], [predicted_sales], color='green', s=150, marker='*', 
            label=f'28℃预测点({predicted_sales}个)', edgecolors='black', linewidth=2)

    plt.title(" 冰淇淋销量预测模型", fontsize=18, pad=20)
    plt.xlabel("温度（℃）", fontsize=14)
    plt.ylabel("销量（个）", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # 保存预测图
    plt.savefig("冰淇淋销量预测模型.png", dpi=300, bbox_inches='tight')
    print(" 预测模型图表已保存为'冰淇淋销量预测模型.png'")

    # 在Debug Console中安全地显示图形
    try:
        plt.show()
    except:
        print(" 无法在当前环境中显示图形窗口，但图片已保存")
        print(" 提示：请查看生成的PNG文件来查看预测模型图表")
        
    plt.close()  # 关闭图形以释放内存

    print(f"\n 模型准确度评分：{model.score(x, y):.3f}")
    print("分析完成！所有图表已保存为PNG文件供查看。")
    
if __name__ == "__main__":
    predict()