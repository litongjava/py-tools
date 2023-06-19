# 使用python3写一个程序 1.获取指定目录下的所有文件名 2.遍历文件名 2.将4-category-template-wps.docx复制到改目录下并重名为相同的文件名,扩展名保留

import os
import shutil

# 获取指定目录下的所有文件名
dir_path = "F:\document\dev-docs\\01_cpp\\02_CPP" # 你需要修改这个路径
template_file = "F:\document\\template\\4-category-template-wps.docx" # 你需要修改这个模板文件的路径和名称
file_names = os.listdir(dir_path) # 这是一个列表，包含了所有文件名

# 遍历文件名
for file_name in file_names:
    if file_name.endswith(".docx"):
        # 将4-category-template-wps.docx复制到该目录下并重命为相同的文件名，扩展名保留
        rpartition = file_name.rpartition(".")
        new_file_name = "new_"+rpartition[0] + ".docx" # 用原来的文件名替换掉模板文件的名称部分，保留.docx扩展名
        new_file_path = os.path.join(dir_path, new_file_name) # 拼接新文件的完整路径
        if not os.path.exists(new_file_path):  # 使用os.path.exists()函数来检查文件是否存在[^1^][1] [^2^][2] [^3^][3]
            shutil.copy(template_file, new_file_path)  # 复制模板文件到新路径，并重命名

print("finished")
#使用python3写一个程序,就旧的doc文档中的所有内容,复制到新的docx文档中