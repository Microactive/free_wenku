import requests
import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error

global doc_url

# 创建主窗口
window = tk.Tk()
window.title('百度文库下载神器')
window.geometry('600x200')

# 设置文档链接输入框
tk.Label(window, text='文档链接:').place(x=50, y=30)
var_doc_url = tk.StringVar()  # 定义变量,用于输入用户名
entry_doc_url = tk.Entry(window, width=60, textvariable=var_doc_url)
entry_doc_url.place(x=110, y=30)

# 设置邮箱输入框
tk.Label(window, text='收件邮箱:').place(x=50, y=70)
var_mailbox = tk.StringVar()  # 定义变量,用于输入用户名
entry_mailbox = tk.Entry(window, width=60, textvariable=var_mailbox).place(x=110, y=70)

# 设置下载进度条
tk.Label(window, text='下载进度:').place(x=50, y=110)
download_progress = tk.StringVar()  # 定义变量,用于输入用户名
entry_download_progress = tk.Entry(window, width=60, textvariable=download_progress).place(x=110, y=110)

# 获取输入的文档链接和邮箱

doc_url = var_doc_url.get()
print(doc_url)
mailbox = var_mailbox.get()

# 清空框内的文档链接
def clear_url():
    entry_doc_url.delete(0, tk.END)
def download():
    global doc_url
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
        'mail': '2280674798@qq.com',
    }

    # 爬虫访问该漏洞，提交携带的数据
    response = requests.request("POST", url, data=datas, headers=header)

    print('下载成功')


# 设置清空链接和一键下载按钮
btn_clear = tk.Button(window, text='清空链接', command=clear_url)
btn_clear.place(x=150, y=150)
btn_download = tk.Button(window, text='一键下载', command=download)
btn_download.place(x=400, y=150)

window.mainloop()