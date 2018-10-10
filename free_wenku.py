import requests

# 构建爬虫，该爬虫模拟浏览器头信息
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

# 获取文档的链接
download_url = input('请输入您要下载文档的地址：')

# 漏洞(通过该漏洞能免券下载百度文库)
url = 'http://39.108.149.27:9999/default.aspx'

# 爬虫要向该漏洞提交的数据
datas = {
    'username': '',
    'password': '',
    'txtUrl': download_url,
    'mail': '2280674798@qq.com'
}

# 爬虫访问该漏洞，提交携带的数据
response = requests.request("POST", url, data=datas, headers=header)

print('下载成功')