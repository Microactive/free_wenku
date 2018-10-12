import requests
import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import threading  # 引入多线程，使程序能同时进行爬虫和进度条显示
import time


# 创建主窗口
window = tk.Tk()
window.title('百度文库下载神器(牛牛定制版)')
window.geometry('630x350')


# 添加背景图
canvas = tk.Canvas(window, height=200, width=600)  # 创建画布
image_file1 = tk.PhotoImage(file='pic1.png')  # 加载图片文件
image = canvas.create_image(230, 20, anchor='nw', image=image_file1)  # 将图片置于画布上
image_file2 = tk.PhotoImage(file='pic2.png')  # 加载图片文件
image = canvas.create_image(310, 25, anchor='nw', image=image_file2)  # 将图片置于画布上
image_file3 = tk.PhotoImage(file='pic3.png')  # 加载图片文件
image = canvas.create_image(130, 120, anchor='nw', image=image_file3)  # 将图片置于画布上
canvas.pack()  # 放置画布


# 设置文档链接输入框
tk.Label(window, text='文档链接:').place(x=50, y=180)
var_doc_url = tk.StringVar()  # 定义变量,用于输入用户名
entry_doc_url = tk.Entry(window, width=66, textvariable=var_doc_url)
entry_doc_url.place(x=110, y=180)

# 设置邮箱输入框
tk.Label(window, text='收件邮箱:').place(x=50, y=220)
var_mailbox = tk.StringVar()  # 定义变量,用于输入用户名
var_mailbox.set('2280674798@qq.com')
entry_mailbox = tk.Entry(window, width=66, textvariable=var_mailbox).place(x=110, y=220)

# # 设置下载进度条
tk.Label(window, text='下载进度:', ).place(x=50, y=260)
canvas = tk.Canvas(window, width=465, height=22, bg="white")
canvas.place(x=110, y=260)

# 显示下载进度
def progress():
    # 填充进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="blue")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数
    for i in range(x):
        n = n + 465 / x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0.02)  # 控制进度条流动的速度

    tk.messagebox.showinfo(  # 通知型弹窗
        title='下载成功',  # 窗口标题
        message='文档已发送，邮箱可能会对其进行拦截，请注意查看垃圾箱',
    )

    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
    x = 500  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数

    for t in range(x):
        n = n + 465 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0)  # 时间为0，即飞速清空进度条

# 清空框内的文档链接
def clear_url():
    entry_doc_url.delete(0, tk.END)

# 下载文档
def download_doc():
    # 获取输入的文档链接和邮箱
    doc_url = str(var_doc_url.get())
    mailbox = str(var_mailbox.get())
    # 构建并伪装爬虫，让对方以为这是来自一般用户的正常访问
    header = {'Accept': 'text/plain, */*; q=0.01',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Connection': 'keep-alive',
              'Content-Length': '135',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': '39.108.149.27:9999',
              'Origin': 'http://39.108.149.27:9999',
              'Referer': 'http://39.108.149.27:9999/',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
              'X-Requested-With': 'XMLHttpRequest'
              }

    # 漏洞
    url = 'http://39.108.149.27:9999/default.aspx'
    # 爬虫要向该漏洞提交的数据
    datas = {
        'username': '',
        'password': '',
        'txtUrl': doc_url,
        'mail': mailbox,
    }
    # 爬虫访问该漏洞，提交携带的数据
    response = requests.request("POST", url, data=datas, headers=header)

threads = []
t1 = threading.Thread(target=progress)
threads.append(t1)
t2 = threading.Thread(target=download_doc)
threads.append(t2)

# 双线程
def two_threading():
    threads = []
    t1 = threading.Thread(target=progress)
    threads.append(t1)
    t2 = threading.Thread(target=download_doc)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()



# 设置清空链接和一键下载按钮
btn_clear = tk.Button(window, text='清空链接', command=clear_url)
btn_clear.place(x=150, y=305)
btn_download = tk.Button(window, text='一键下载', command=two_threading)
btn_download.place(x=400, y=305)

window.mainloop()