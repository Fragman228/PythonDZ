import requests
body = {

}
response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies)

print(response.text)
with open("page.html","w", encoding="UTF -8") as f:
    f.write(response.text)
    bs = BeautifulSoup()
    containers = bs.find