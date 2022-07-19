# 请求库
import requests
# 解析库
from bs4 import BeautifulSoup
# 用于解决爬取的数据格式化
import io
import sys

# 抓取刘涛的照片：https://movie.douban.com/celebrity/1011562/photos/
import requests

url = 'https://movie.douban.com/celebrity/1011562/photos/'
r= requests.get(url)
print(r.status_code)