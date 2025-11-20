""" 
实例对象及方法：
cap（cv2.VideoCapture 实例）：
cap.read()
cap.release()
函数：
cv2.flip()
cv2.putText()
cv2.imshow()
cv2.waitKey()
cv2.destroyAllWindows() """

import cv2

cap = cv2.VideoCapture(0)
while True:
    s, img = cap.read()
    img = cv2.flip(img, 1)  #flip传入两个参数，第一个就是图像，其中输入1代表水平翻转，同学们也可尝试一下0，-1这两个值，看看会有什么效果    
    cv2.putText(img, "Hello", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    #（图像、文字内容、位置、字体(cv2.FONT_HERSHEY_SIMPLEX)、大小、颜色，粗细（选传））
    cv2.imshow('image',img)  #放在后面以将画面更新为最新结果
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()#两行Opencv收尾代码，用来结束程序资源占用