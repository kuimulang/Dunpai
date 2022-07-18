import requests

res = requests.post('http://www.xxxx.com')
print(res)
print(type(res))
print(type(res.text))

print(res.text)

# def post(url: str | bytes,
#          data: Any = ...,
#          json: Any | None = ...,
#          params: Any = ...,
#          headers: Any | None = ...,
#          cookies: Any | None = ...,
#          files: Any | None = ...,
#          auth: Any | None = ...,
#          timeout: Any | None = ...,
#          allow_redirects: bool = ...,
#          proxies: Any | None = ...,
#          hooks: Any | None = ...,
#          stream: Any | None = ...,
#          verify: Any | None = ...,
#          cert: Any | None = ...)