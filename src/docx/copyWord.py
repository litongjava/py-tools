# 导入docx库
from docx import Document

# 打开输入和输出文档
# input_file =
output_docx = "F:\\document\\dev-docs\\01_cpp\\02_CPP\\C++_03.cmake.docx"
input_doc = Document("input.doc")
output_doc = Document()

# 遍历输入文档的段落或表格，并将它们添加到输出文档中
for para in input_doc.paragraphs:
    output_doc.add_paragraph(para.text)

for table in input_doc.tables:
    output_doc.add_table(table)

# 解压输入文档的.docx文件，提取其中的图片，并保存到文件系统中
import zipfile

with zipfile.ZipFile("input.docx", "r") as z:
    for file in z.namelist():
        if file.startswith("word/media/"):
            z.extract(file, "images")

# 在输出文档中使用document.add_picture()方法添加图片
from docx.shared import Inches

output_doc.add_picture("images/word/media/image1.png", width=Inches(1.25))

# 保存输出文档
output_doc.save(output_docx)
