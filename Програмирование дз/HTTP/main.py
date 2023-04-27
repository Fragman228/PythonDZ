import requests

uls = ['https://cataas.com/cat', 'https://cataas.com/cat?type=:original', 'https://cataas.com/cat?filter=:pixel']
cats = uls * 2

for i in range(1, len(cats)+1):
    url = cats[i - 1]
    b = requests.get(url)
    with open(f"cat{i}.jpg", "wb") as fb:
        fb.write(b.content)
        fb.close()



