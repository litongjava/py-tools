from PIL import Image, ImageDraw, ImageFont

# 设置图片大小和背景色
size = (512, 512)
bg_color = (255, 255, 255, 0)

# 创建一个空白的RGBA模式的图片
img = Image.new('RGBA', size, bg_color)

# 创建一个ImageDraw对象
draw = ImageDraw.Draw(img)

# 设置字体和字体大小
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 200)

# 设置文字内容和颜色
text = 'Chat\nGPT'
text_color = (0, 0, 0, 255)

# 计算文字的宽度和高度
text_size = draw.textsize(text, font)

# 计算文字的位置
text_x = (size[0] - text_size[0]) / 2
text_y = (size[1] - text_size[1]) / 2

# 在图片上绘制文字
draw.text((text_x, text_y), text, fill=text_color, font=font)

# 保存图片为ico格式
img.save('custom_icon.ico')
img.save('custom_icon.png')
# img.save('custom_icon.ico', sizes=[(16, 16), (32, 32)])