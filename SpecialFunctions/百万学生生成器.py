#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名：generate_million_students.py
程序功能：生成百万个学生数据，用于测试学生通信录管理系统
作者：Assistant
完成日期：2025年10月
版本：1.0
"""

import random
import time
from datetime import datetime, timedelta
import os

class StudentDataGenerator:
    def __init__(self):
        # 初始化数据池
        self.first_names = [
            '张', '王', '李', '赵', '陈', '刘', '杨', '黄', '周', '吴',
            '徐', '孙', '胡', '朱', '高', '林', '何', '郭', '马', '罗',
            '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于', '董', '萧'
        ]
        
        self.last_names = [
            '伟', '芳', '娜', '秀英', '敏', '静', '丽', '强', '磊', '军',
            '洋', '勇', '艳', '杰', '娟', '涛', '明', '超', '秀兰', '霞',
            '平', '刚', '桂英', '建华', '亮', '健', '雪', '燕', '鑫', '婷'
        ]
        
        self.addresses = [
            '北京市海淀区中关村大街', '上海市浦东新区陆家嘴', '广州市天河区珠江新城',
            '深圳市南山区科技园', '杭州市西湖区文三路', '南京市鼓楼区中山路',
            '武汉市武昌区光谷', '成都市武侯区天府大道', '西安市雁塔区高新路',
            '重庆市渝中区解放碑', '天津市和平区南京路', '苏州市工业园区金鸡湖大道',
            '长沙市岳麓区麓谷', '郑州市金水区花园路', '青岛市市南区香港中路'
        ]
        
        self.area_codes = ['010', '021', '022', '023', '024', '025', '027', '028', '029']
        
    def generate_id(self, index):
        """生成学号，格式：年份+序号"""
        year = random.randint(2020, 2024)
        return f"{year}{index:07d}"
    
    def generate_name(self):
        """生成姓名"""
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return first_name + last_name
    
    def generate_birth_date(self):
        """生成出生日期（18-25岁）"""
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2007, 12, 31)
        random_days = random.randint(0, (end_date - start_date).days)
        birth_date = start_date + timedelta(days=random_days)
        return birth_date.strftime("%Y-%m-%d")
    
    def generate_gender(self):
        """生成性别"""
        return random.choice(['男', '女'])
    
    def generate_address(self):
        """生成地址"""
        address = random.choice(self.addresses)
        street_number = random.randint(1, 999)
        return f"{address}{street_number}号"
    
    def generate_coordinates(self):
        """生成坐标（中国范围内的合理坐标）"""
        # 中国大致经纬度范围
        x = round(random.uniform(73.66, 135.05), 6)  # 经度
        y = round(random.uniform(18.15, 53.55), 6)    # 纬度
        return x, y
    
    def generate_phone(self, index):
        """生成电话号码"""
        area_code = random.choice(self.area_codes)
        # 确保电话号码唯一
        base_number = 10000000 + (index % 90000000)
        return f"{area_code}-{base_number:08d}"
    
    def generate_student(self, index):
        """生成单个学生数据"""
        id = self.generate_id(index)
        name = self.generate_name()
        birth = self.generate_birth_date()
        gender = self.generate_gender()
        address = self.generate_address()
        x, y = self.generate_coordinates()
        phone = self.generate_phone(index)
        
        return {
            'id': id,
            'name': name,
            'birth': birth,
            'gender': gender,
            'address': address,
            'x': x,
            'y': y,
            'phone': phone
        }
    
    def generate_million_students(self, count=1000000):
        """保持兼容的旧方法：按批次生成并保存到多个文件（保留不变）"""
        print(f"开始生成 {count} 个学生数据（分文件模式）...")
        batch_size = 50000
        for batch_start in range(0, count, batch_size):
            batch_end = min(batch_start + batch_size, count)
            print(f"生成批次: {batch_start + 1} - {batch_end}")

            students = []
            for i in range(batch_start, batch_end):
                student = self.generate_student(i)
                students.append(student)

            filename = f"students_data_{batch_start+1}_{batch_end}.txt"
            self.save_to_file(students, filename)

        print("所有数据生成完成！")

    def generate_to_single_file(self, filename: str = "students_all.txt", count: int = 1000000, batch_size: int = 50000):
        """将所有生成的数据写入同一个文件（流式写入，节省内存）"""
        print(f"开始生成 {count} 个学生数据，写入文件：{filename}")
        os.makedirs(os.path.dirname(os.path.abspath(filename)) or ".", exist_ok=True)

        start_time = time.time()
        written = 0
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\ufeff')  # 可选 BOM
            for batch_start in range(0, count, batch_size):
                batch_end = min(batch_start + batch_size, count)
                # 生成并直接写入该批次，避免把整批保存在内存
                for i in range(batch_start, batch_end):
                    student = self.generate_student(i)
                    line = f"{student['id']}|{student['name']}|{student['birth']}|" \
                           f"{student['gender']}|{student['address']}|" \
                           f"{student['x']}|{student['y']}|{student['phone']}\n"
                    f.write(line)
                    written += 1

                # 显示进度
                print(f"已写入: {written}/{count} ({written/count*100:.1f}%)")

        end_time = time.time()
        print(f"数据生成完成！耗时: {end_time - start_time:.2f} 秒")
        print(f"输出文件: {os.path.abspath(filename)} 大小: {os.path.getsize(filename)/(1024*1024):.2f} MB")

    def generate_million_students(self, count=1000000):
        """生成指定数量的学生数据（按批次生成并立即保存）"""
        print(f"开始生成 {count} 个学生数据...")

        batch_size = 50000

        for batch_start in range(0, count, batch_size):
            batch_end = min(batch_start + batch_size, count)
            print(f"生成批次: {batch_start + 1} - {batch_end}")

            students = []
            for i in range(batch_start, batch_end):
                student = self.generate_student(i)
                students.append(student)

            # 使用包含序号范围的唯一文件名，避免覆盖
            filename = f"students_data_{batch_start+1}_{batch_end}.txt"
            self.save_to_file(students, filename)

        print("所有数据生成完成！")

def validate_data(filename, sample_size=1000):
    """验证生成的数据格式"""
    print(f"\n验证数据文件: {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"总行数: {len(lines)}")
    
    # 检查前几行样本
    for i in range(min(sample_size, len(lines))):
        line = lines[i].strip()
        if line.startswith('\ufeff'):
            line = line[1:]  # 去除BOM
        
        parts = line.split('|')
        if len(parts) != 8:
            print(f"第{i+1}行格式错误: {line}")
            continue
        
        id, name, birth, gender, address, x, y, phone = parts
        
        # 基本验证
        try:
            float(x)
            float(y)
            # 检查日期格式
            datetime.strptime(birth, "%Y-%m-%d")
        except ValueError as e:
            print(f"第{i+1}行数据格式异常: {e}")
    
    print("数据验证完成！")

def main():
    """主函数"""
    print("=" * 60)
    print("百万学生数据生成器")
    print("=" * 60)
    
    generator = StudentDataGenerator()
    
    # 用户选择生成数量
    while True:
        try:
            count = int(input("请输入要生成的学生数量 (默认100万): ") or "1000000")
            if count <= 0:
                print("请输入正整数！")
                continue
            break
        except ValueError:
            print("请输入有效的数字！")
    
    # 选择输出到单个文件
    out_file = input("输出文件名（默认 students_all.txt）：").strip() or "students_all.txt"

    # 生成数据到单个文件
    generator.generate_to_single_file(out_file, count)

    # 验证数据（可选）
    validate_choice = input("是否验证生成的数据？(y/n, 默认n): ").lower()
    if validate_choice == 'y':
        validate_data(out_file)
    
    print("\n数据生成任务完成！")

if __name__ == "__main__":
    main()