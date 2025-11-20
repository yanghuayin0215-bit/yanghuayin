""" 实例对象（类名）：
- root（tk.Tk）
- entry（tk.Entry）
- lable（tk.Label）
- button（tk.Button）

方法：
- tk.Tk().geometry()
- tk.Tk().title()
- tk.Entry().pack()
- tk.Label().pack()
- tk.Button().pack()
- tk.Tk().mainloop()
- mgb.showinfo()

函数：
- greet() """

import tkinter as tk
from tkinter import messagebox as mgb
#加入主窗口
root = tk.Tk()
root.title('简单交互')
root.geometry('300x200')
def greet():
    name = entry.get()
    mgb.showinfo('问候',f"hello,{name}")
#entry加入输入框
entry = tk.Entry()
entry.pack(pady=5)
#lable加入提示标签
lable = tk.Label(text='请输入你的名字' )
lable.pack(pady=5)
#button加入按钮完成交互
button = tk.Button(text='点击问候',command=greet)
button.pack(pady=5)
root.mainloop()