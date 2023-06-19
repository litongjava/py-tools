import PyPDF2

# 打开PDF文件
pdfFilePath = r'F:\document\dev-docs\17_Python\02_python_基础类库\GUI图形用户界面编程.pdf'
with open(pdfFilePath, 'rb') as f:
    # 创建一个PdfFileReader对象
    pdf_reader = PyPDF2.PdfReader(f)
    # 获取PDF文件的总页数
    num_pages = len(pdf_reader.pages)
    # 遍历每一页PDF文档
    for i in range(num_pages):
        # 获取当前页
        page = pdf_reader.pages[i]
        # 提取文本内容
        text = page.extract_text()
        # 输出文本内容
        print(text)

# 关闭PDF文件
f.close()