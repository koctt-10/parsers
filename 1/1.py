import requests
from apikey import API_TOKEN

data = {
"custname": "hfgdhdf",
"custtel" : "64546645",
"custemail": "hfgdshgfd@m.com",
"size": "medium",
"topping": "bacon",
"topping": "cheese",
"topping": "onion",
"delivery": "20:00",
"comments": "gfdgfd"
}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-65daff49-175c89076da8703d3db489a9"
}

variable = requests.Session()

aaa = variable.get("https://httpbin.org/post")

response = variable.post('https://httpbin.org/post', headers=headers, data=data)


    
#print(response.status_code)
#print(response.headers)
#print(response.text)