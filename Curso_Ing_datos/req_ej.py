import requests
import bs4

response=requests.get("https://elpais.com/america-colombia/")
response.encoding="utf-8"
soup=bs4.BeautifulSoup(response.text,"html.parser")
link_noticias=soup.select(".c_t a")
noticias=[i["href"] for i in link_noticias]
print(noticias)