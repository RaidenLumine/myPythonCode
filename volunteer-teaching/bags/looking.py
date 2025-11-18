import matplotlib.pyplot as plt
import matplotlib
def looking():
    try:
        matplotlib.use('TkAgg')  # 尝试使用交互式后端
    except:
        matplotlib.use('Agg')    # 如果失败，使用非交互式后端
        
    # 配置中文字体支持
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    # 数据
    temp = [22, 25, 28, 30, 18]  # 温度
    sales = [15, 30, 50, 60, 10]  # 销量

    plt.figure(figsize=(10, 6))  # 设置图形大小
    plt.scatter(temp, sales, color='red', s=100)  # 调大点尺寸便于观察
    plt.title("冰淇淋销量侦探报告", fontsize=16)
    plt.xlabel("温度（℃）→ 线索", fontsize=12)  # X轴
    plt.ylabel("销量（个）→ 结果", fontsize=12)  # Y轴
    plt.grid(True, alpha=0.3)  # 添加网格线
    plt.tight_layout() # 自动调整布局

    # 同时保存图片和尝试显示
    plt.savefig("冰淇淋销量分析.png", dpi=300, bbox_inches='tight')
    print(" 图表已保存为'冰淇淋销量分析.png'")

    # 在Debug Console中安全地显示图形
    try:
        plt.show()
    except:
        print(" 无法在当前环境中显示图形窗口，但图片已保存")
        print(" 提示：请查看生成的PNG文件来查看图表")
        
    plt.close()  # 关闭图形以释放内存
    
if __name__ == "__main__":
    looking()