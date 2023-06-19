import cv2

img = cv2.imread(r'E:\code\frontend\project-litongjava\electron-openai-chatgpt\src\images\logo-512x512.png')
resized_img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('resized_image.jpg', resized_img)
