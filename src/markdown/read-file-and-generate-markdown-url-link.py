# 从input.txt中读取文件
with open('input-link.txt', 'r') as file:
    content = file.readlines()

# 生成Markdown格式的链接
markdown_links = []
for line in content:
    line = line.strip()  # 去除换行符和空格
    link_parts = line.split('/')
    name = link_parts[-3]
    url = line
    markdown_link = f'- [{name}]({url})'
    markdown_links.append(markdown_link)

# 打印生成的Markdown链接
for link in markdown_links:
    print(link)
