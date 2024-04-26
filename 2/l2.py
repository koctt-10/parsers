import requests
from bs4 import BeautifulSoup
from time import sleep


#list_card_url = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

def get_url():
    for count in range(1,8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"


        responce = requests.get(url, headers=headers)

        soup = BeautifulSoup(responce.text, 'lxml') #html.parcer


        data = soup.find_all('div', class_="w-full rounded border")

        for i in data:
            
            card_url = "https://scrapingclub.com" + i.find('a').get('href')
            #list_card_url.append(card_url)
            #name = i.find('h4', class_='p-4') 
            #price = i.find('h5').text
            #url_img = 'https://scrapingclub.com' + i.find('img', class_="card-img-top img-fluid").get('src')
            
            #print(*list_card_url)
            #print("\n" + price + "\n" + url_img + "\n")
            yield card_url
        #print(*list_card_url)  

def array():
    for card_url in get_url():
        responce = requests.get(card_url, headers=headers)

        sleep(0.0005)
        soup = BeautifulSoup(responce.text, 'lxml')

        data = soup.find('div', class_="my-8 w-full rounded border")
        
        name = data.find('h3',class_='card-title').text
        price = data.find('h4').text
        text = data.find('p', class_='card-description').text
        url_img = "https://scrapingclub.com" + data.find('img', class_='card-img-top').get('src')
        
        yield name, price, text, url_img