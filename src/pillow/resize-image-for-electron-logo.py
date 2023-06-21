import os.path

from PIL import Image

# 读取原始图像
srcImage = r"F:\code\frontend\project-litongjava\electron-google-translate\build\Google_Translate_logo.svg.png"
dirname = os.path.dirname(srcImage)

# 输出不同尺寸的图像
# Image.open(srcImage).resize((256, 256)).save(os.path.join(dirname, "icon.ico"))
srcImage = Image.open(srcImage)
srcImage.save(os.path.join(dirname, "icon.ico"), formats="ICO", sizes=[(256, 256)])
srcImage.resize((256, 256)).save(os.path.join(dirname, "icon.png"))
srcImage.resize((1024, 1024)).save(os.path.join(dirname, "icon.icns"))
