import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps

# 1. 加载和预处理MNIST数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 归一化和重塑数据 (28x28像素，灰度图)
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# 转换标签为独热编码
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 2. 构建CNN模型
def build_model():
    model = models.Sequential([
        # 第一个卷积层
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        
        # 第二个卷积层
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # 第三个卷积层 
        layers.Conv2D(64, (3, 3), activation='relu'),
        
        # 新增第四个卷积层 - 增加模型深度
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),  
        
        # 全连接层
        layers.Flatten(),
        layers.Dense(128, activation='relu'),  # 修改2：增加全连接层神经元数量
        layers.Dense(64, activation='relu'),   # 修改3：新增一个全连接层
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# 检查是否已有保存的模型，如果没有则训练新模型
try:
    model = tf.keras.models.load_model('mnist_model.h5')
    print("已加载已保存的模型")
except:
    print("没有找到已保存的模型，开始训练新模型...")
    model = build_model()
    # 训练模型，增加训练轮次
    model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2)  # 修改4：epochs从5增加到10，验证集改为0.2
    
    # 评估模型在测试集上的表现
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"测试集准确率: {test_acc:.4f}")
    
    # 保存模型供后续使用
    model.save('mnist_model.h5')
    print("模型已保存为 mnist_model.h5")

# 3. 创建手写界面（以下部分未修改）
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("手写数字识别")
        
        # 创建画布
        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, 
                               bg='white', highlightthickness=2, highlightbackground='gray')
        self.canvas.pack(padx=10, pady=10)
        
        # 创建绘图对象
        self.image = Image.new('L', (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)
        
        # 绑定鼠标事件
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_pos)
        
        # 创建按钮区域
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.predict_btn = tk.Button(self.buttons_frame, text="识别数字", 
                                    command=self.predict_digit, font=('Arial', 12))
        self.predict_btn.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.clear_btn = tk.Button(self.buttons_frame, text="清除画布", 
                                  command=self.clear_canvas, font=('Arial', 12))
        self.clear_btn.pack(side=tk.LEFT, padx=10, pady=5)
        
        # 结果显示区域
        self.result_var = tk.StringVar()
        self.result_var.set("请在画布上用鼠标写一个数字，然后点击'识别数字'")
        self.result_label = tk.Label(root, textvariable=self.result_var, 
                                    font=('Arial', 14), fg='blue')
        self.result_label.pack(pady=10)
        
        self.last_x = None
        self.last_y = None

    def draw_lines(self, event):
        """处理鼠标拖动事件，绘制线条"""
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            # 在画布上绘制可见线条
            self.canvas.create_line(self.last_x, self.last_y, x, y, 
                                   width=15, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
            # 在图像对象上绘制线条（用于后续识别）
            self.draw.line([self.last_x, self.last_y, x, y], fill=0, width=15)
        self.last_x = x
        self.last_y = y

    def reset_last_pos(self, event):
        """重置最后位置，避免线条连在一起"""
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        """清除画布内容"""
        self.canvas.delete("all")
        self.image = Image.new('L', (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.result_var.set("请在画布上用鼠标写一个数字，然后点击'识别数字'")

    def predict_digit(self):
        """识别手写数字"""
        # 处理图像：调整大小为28x28，反转颜色（MNIST是黑底白字）
        img = self.image.resize((28, 28))
        img = ImageOps.invert(img)
        img = np.array(img)
        
        # 归一化并调整形状以适应模型输入
        img = img.reshape(1, 28, 28, 1).astype('float32') / 255.0
        
        # 进行预测
        prediction = model.predict(img)
        digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        # 显示结果
        self.result_var.set(f"识别结果: {digit}，可信度: {confidence:.2f}%")

# 4. 运行应用程序
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()