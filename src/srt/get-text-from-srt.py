# 使用python语言编写一个程序,从srt字幕文件中提取出文字,只要文字信息,不要序号和时间信息
import sys
def getText(filepath):
    global text_list, text
    with open(filepath, 'r',encoding='utf-8') as f:
        content = f.readlines()
    text_list = []
    for i in range(0, len(content), 4):
        # 剔除行首的序号和时间信息,所以直接取第三行即可
        text = content[i + 2].strip()
        text_list.append(text)

    text = ' '.join(text_list)
    print(text)

# filepath = '/Users/ping/Movies/4K Video Downloader/The Importance of Culture in Tourism.en.srt'
# getText(filepath)

if __name__ == "__main__":
    if sys.argv[1] is not None:
        getText(sys.argv[1])

