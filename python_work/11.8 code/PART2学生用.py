import cv2
from cvzone.HandTrackingModule import HandDetector


""" cap（cv2.VideoCapture 实例）：
cap.read()
cap.release()
handdet（HandDetector 实例）：
handdet.findHands()
handdet.findDistance()
函数：
cv2.flip()
cv2.putText()（图像、文字内容、位置、字体(cv2.FONT_HERSHEY_SIMPLEX)、大小、颜色，粗细（选传））
cv2.imshow()
cv2.waitKey()
cv2.destroyAllWindows() """
#利用函数有read,flip,findHands,findDistance,putText（图像、文字内容、位置、字体(cv2.FONT_HERSHEY_SIMPLEX)、
# 大小、颜色，粗细（选传）），imshow,waitKey

cap = cv2.VideoCapture(0)
c = 0
handdet = HandDetector(detectionCon = 0.8)


while True:
    s,img = cap.read()
    img = cv2.flip(img, 1)
    hands,img = handdet.findHands(img)
    if hands:
        muzhi = hands[0]['lmList'][4][:2]
        shizhi = hands[0]['lmList'][8][:2]
        distance = handdet.findDistance(muzhi,shizhi)[0]
    ####begin
    ####想想怎么样修改可以使仅在手指夹在一起后记录一次
    
        if distance < 40:
            c += 1

    ####end

    cv2.putText(img,f'score = {c}',(20,30),(cv2.FONT_HERSHEY_SIMPLEX),1.5,(0,255,0),3)
    cv2.imshow('counter',img)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
