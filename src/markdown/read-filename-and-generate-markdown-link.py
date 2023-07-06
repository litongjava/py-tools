# mathematical-knowledge有一个文件夹,它下面有有些pdf文件
# 读取F:\code\markdown\project\mathematical-knowledge目录下的文件,生成下面的格式
# 使用python语言
# - [1.1_Squares, Cubes, and Beyond.pdf](mathematical-knowledge/1.1_Squares, Cubes, and Beyond.pdf)
import os
from urllib.parse import quote


def list_files(directory):
    file_paths = []
    listdir = os.listdir(directory)
    for file_name in listdir:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
        else:
            file_paths.extend(list_files(file_path))

    return file_paths


directory = r"F:\code\markdown\project\mathematical-knowledge"
files = list_files(directory)
for file_path in files:
    if os.path.isfile(file_path):
        relative_path = os.path.relpath(file_path, directory)
        relative_path=relative_path.replace("\\","/")
        file_name = os.path.basename(file_path)
        if file_name == "readme.md":
            continue
        formatted_name = f"- [{file_name}]({quote(relative_path)})"
        print(formatted_name)
