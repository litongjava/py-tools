import os.path

from PIL import Image

# 读取原始图像
srcImage = r"E:\code\google-chrome-extensions\project-litongjava\google-chrome-apps-chatgpt\icons\src.png"
dirname = os.path.dirname(srcImage)

# 输出不同尺寸的图像
# Image.open(srcImage).resize((256, 256)).save(os.path.join(dirname, "icon.ico"))
srcImage = Image.open(srcImage)
srcImage.resize((16, 16)).save(os.path.join(dirname, "icon16.png"))
srcImage.resize((48, 48)).save(os.path.join(dirname, "icon48.png"))
srcImage.resize((128, 128)).save(os.path.join(dirname, "icon128.png"))
print("done")