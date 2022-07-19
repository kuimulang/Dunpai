# 抓取刘涛的照片：https://movie.douban.com/celebrity/1011562/photos/
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/celebrity/1011562/photos/'
res = requests.get(url).text
print(res)
content = BeautifulSoup(res, "html.parser")
data = content.find_all('div', attrs={'class': 'cover'})
picture_list = []
for d in data:
    plist = d.find('img')['src']
    picture_list.append(plist)
print(picture_list)

# def find_all(self,
#              name: str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool | Iterable[str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool] = ...,
#              attrs: Dict[str, str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool | Iterable[str | bool | None | bytes | Pattern[str] | (...) -> bool | ...]] | str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool | Iterable[str | bool | None | bytes | Pattern[str] | (...) -> bool | ...] = ...,
#              recursive: bool = ...,
#              text: str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool | Iterable[str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool] = ...,
#              limit: int | None = ...,
#              **kwargs: str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool | Iterable[str | bool | None | bytes | Pattern[str] | (str) -> bool | (Tag) -> bool])


