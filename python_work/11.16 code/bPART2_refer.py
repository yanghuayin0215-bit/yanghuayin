import tkinter as tk
from tkinter import messagebox as mgb

root = tk.Tk()
root.geometry("300x100")
root.title('打招呼小程序')
####begin
#尝试修改为若不输入，弹出框框名为提示，内容为请输入你的名字
""" def greet():
    name = entry.get()
    mgb.showinfo('greet',f'hello,{name}') """
def greet():
    name = entry.get()
    if not name:
        mgb.showinfo('提示','请输入你的名字')
    else:
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