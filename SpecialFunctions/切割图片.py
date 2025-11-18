import os
from PIL import Image

def split_image(image_path, output_folder, grid_size=(4, 4)):
    img = Image.open(image_path)
    width, height = img.size
    grid_width, grid_height = grid_size
    cell_width = width // grid_width
    cell_height = height // grid_height

    # 创建对应的子文件夹
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    sub_folder = os.path.join(output_folder, name)
    os.makedirs(sub_folder, exist_ok=True)

    # 分割图片并保存
    count = 1
    for i in range(grid_height):
        for j in range(grid_width):
            if i == grid_height - 1 and j == grid_width - 1:
                # 跳过最右下角的小图片
                continue
            left = j * cell_width
            upper = i * cell_height
            right = left + cell_width
            lower = upper + cell_height
            cell = img.crop((left, upper, right, lower))
            cell.save(os.path.join(sub_folder, f"{count}{ext}"))
            count += 1

def process_folder(input_folder, output_folder):
    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            split_image(image_path, output_folder)

# 使用示例（以下路径随时可以修改）
input_folder = "E:\\我的图片\\mygo_mujica"  # 替换为你的输入文件夹路径
output_folder = "E:\\我的图片\\mygo_mujica"  # 替换为你的输出文件夹路径
process_folder(input_folder, output_folder)