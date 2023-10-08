import os.path

from PIL import Image

# 读取原始图像
srcImage = r"F:\code\rust\project-litongjava\tauri-magic-web\src\logo\src.png"
dirname = os.path.dirname(srcImage)
image = Image.open(srcImage)

# Reduce color depth to 8 bits (256 colors)
image = image.quantize()

# 保存为 ICO 文件
# 16 × 16 (256 colors) - Ordinal name: 1
# 32 × 32 (256 colors) - Ordinal name: 2
# 48 × 48 (256 colors) - Ordinal name: 3
image.save(os.path.join(dirname, "icon256.ico"), formats="ICO",
           sizes=[(16, 16), (32, 32), (48, 48)])

# 16 × 16 (16.8mil colors) - Ordinal name: 4
# 32 × 32 (16.8mil colors) - Ordinal name: 5
# 48 × 48 (16.8mil colors) - Ordinal name: 6
# 256 × 256 (16.8mil colors) - Ordinal name: 7
image = Image.open(srcImage)
image.save(os.path.join(dirname, "icon.ico"), formats="ICO",
           sizes=[(16, 16), (32, 32), (48, 48),(16, 16), (32, 32), (48, 48), (256, 256)])
