import tkinter as tk
from tkinter import messagebox as mgb

root = tk.Tk()
root.geometry("300x100")
root.title('打招呼小程序')
####begin
#尝试修改，以实现直到用户输入后才进行打招呼
def greet():
    name = entry.get()
    mgb.showinfo('greet',f'hello,{name}')
####end
#entry加入输入框
entry = tk.Entry()
entry.pack(pady=5)
#lable加入提示标签
lable = tk.Label(text='请输入你的名字')
lable.pack(pady=5)
#button加入按钮完成交互
button = tk.Button(text='点击问候',command = greet)
button.pack(pady=5)
root.mainloop()