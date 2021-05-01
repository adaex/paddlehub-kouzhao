import cv2

img = cv2.imread("images/1.jpg")    # 读取一张图像
cv2.imshow("my image", img)     # 显示图片窗口
cv2.waitKey()   # 阻塞等待按键
cv2.destroyAllWindows()     # 销毁资源