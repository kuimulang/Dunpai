import requests
# 爬取豆瓣网的图片

print("======================")
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36'
}

url = 'http://www.douban.com'
res = requests.get(url,headers=headers)
print(res.status_code)


print("======================")
res = requests.get('http://www.douban.com')
print(res)
print(type(res))
print(type(res.text))

print(res.text)

