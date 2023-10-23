import bs4
import requests

result = requests.get(
    "https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9"
)
soup = bs4.BeautifulSoup(result.text, 'lxml')
image = soup.select("img.mw-file-element")
for i in range(len(image)):
    print(i)
    print(image[i]["src"])


result2 = requests.get(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Kings_Cross_Platform_9%2C75.jpg/220px-Kings_Cross_Platform_9%2C75.jpg"
)
with open("harry_image.jpg", "wb") as f:
    f.write(result2.content)
   

