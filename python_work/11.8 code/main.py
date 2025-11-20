""" 确保你有一个名为 "donut.png" 的食物图片在代码同一目录下，或者修改代码中对应的路径
运行程序后，摄像头会启动
用你的手在摄像头前移动，食指指尖将控制蛇的移动方向
让蛇吃到食物来得分
捏合食指和大拇指可以重置游戏
按 ESC 键退出程序 """

import math
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

#面部识别
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#马赛克
def apply_mosaic(img, top_left, bottom_right, mosaic_size):
    (x1, y1), (x2, y2) = top_left, bottom_right
    roi = img[y1:y2, x1:x2]
    # 计算每个小块的大小
    w, h = (x2 - x1) // mosaic_size, (y2 - y1) // mosaic_size
    for i in range(0, x2 - x1, w):
        for j in range(0, y2 - y1, h):
            rect = [i + x1, j + y1, w, h]
            # 获取每个小块的颜色值
            color = img[j + y1 + h // 2, i + x1 + w // 2]
            # 填充小块
            cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), color.tolist(), -1)
    return img

cap = cv2.VideoCapture(0) #0为自己的摄像头
# cap = cv2.VideoCapture(r'G:\SnakeGame\demo1.mp4')

# cap.set(3, 1280)        # 宽 
# cap.set(4, 720)         # 高

# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)


detector = HandDetector(detectionCon=0.8, maxHands=1)

class SnakeGameClass:
    def __init__(self,pathFood):    # 构造方法
        self.points = []            # 蛇身上所有的点
        self.lengths = []           # 每个点之间的长度
        self.currentLength = 0      # 蛇的总长
        self.allowedLength = 150    # 蛇允许的总长度
        self.previousHead = 0, 0    # 第二个头结点

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood , _= self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

        self.score = 0
        self.gameOver = False

    # def randomFoodLocation(self):
    #     self.foodPoint = random.randint(100, 500), random.randint(100, 600)
    def randomFoodLocation(self):
        self.foodPoint = random.randint(self.wFood//2, 640 - self.wFood//2), random.randint(self.hFood//2, 480 - self.hFood//2)


    def update(self, imgMain, currentHead):     # 实例方法

        if self.gameOver:
            cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                               scale=3, thickness=5, offset=20)
            cvzone.putTextRect(imgMain, f'Your Score:{self.score}', [250, 300],
                               scale=3, thickness=5, offset=20)
        else:
            px, py = self.previousHead
            cx, cy = currentHead

            self.points.append([cx, cy])             # 添加蛇的点列表节点
            distance = math.hypot(cx - px, cy - py)  # 两点之间的距离
            self.lengths.append(distance)            # 添加蛇的距离列表内容
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length Reduction 收缩长度
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

            # Check if snake ate the food 是否吃了食物
            rx, ry = self.foodPoint
            # if rx < cx < rx + self.wFood and ry < cy < ry + self.hFood:
            #     print("ate")
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                print(self.score)

            # Draw Snake 画蛇
            if self.points:
                for i, point in enumerate(self.points):
                     if i != 0:
                        self.points[i-1] = tuple(self.points[i-1])  # 转换数据格式22
                        self.points[i] = tuple(self.points[i])  # 转换数据格式22
                        cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                # 对列表最后一个点也就是蛇头画为紫色点

                self.points[-1] = tuple(self.points[-1])  # 转换数据格式22
                cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            # Draw Food 画食物
            # rx, ry = self.foodPoint
            imgMain = cvzone.overlayPNG(imgMain, self.imgFood,(rx - self.wFood // 2, ry - self.hFood // 2))

            cvzone.putTextRect(imgMain, f'Your Score:{self.score}', [50, 80],scale=3, thickness=5, offset=10)

            # Check for Collision 检查是否缠绕
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))  # 重塑为一个行数未知但只有一列且每个元素有2个子元素的矩阵
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            # 第三个参数是False，我们得到的是不闭合的线
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            print(minDist)
            # 参数True表示输出该像素点到轮廓最近距离

            if -1 <= minDist <= 1:
                print("Hit")
                self.gameOver = True
                self.points = []  # 蛇身上所有的点
                self.lengths = []  # 每个点之间的长度
                self.currentLength = 0  # 蛇的总长
                self.allowedLength = 150  # 蛇允许的总长度
                self.previousHead = 0, 0  # 第二个头结点
                self.randomFoodLocation()


        return imgMain

game = SnakeGameClass("nuaa.png")


while True:
    success, img = cap.read()
    # img = cv2.resize(img,(1920,1080))
    img = cv2.flip(img, 1)  # 将手水平翻转
    hands, img = detector.findHands(img, flipType=False)  # 左手是左手，右手是右手，映射正确

    distance = 41    

    if hands:
        lmList = hands[0]['lmList']     # hands是由N个字典组成的列表
        pointIndex = lmList[8][0:2]     # 只要食指指尖的x和y坐标
        pointThumb = lmList[4][0:2]  # 大拇指指尖
        distance = math.hypot(pointIndex[0] - pointThumb[0], pointIndex[1] - pointThumb[1])
        pointIndex = tuple(pointIndex)  #转换数据格式22
        # print(type(img))
        # cv2.circle(img, pointIndex, 20, (200, 0, 200), cv2.FILLED)
        img = game.update(img,pointIndex)

    # 人脸检测
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 为每个检测到的人脸应用马赛克
    for (x, y, w, h) in faces:
        img = apply_mosaic(img, (x, y), (x + w, y + h), 15)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)

    if distance < 40:  # 如果食指和大拇指的距离小于40像素，则重置游戏
        key = ord('r')  

    if key == ord('r'):
        game.gameOver = False
    elif key == 27:
        #释放内存
        cv2.destroyAllWindows()
        #释放摄像头
        cap.release()
        break
