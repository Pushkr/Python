import requests
from bs4 import BeautifulSoup

url = "https://newjersey.craigslist.org"
search_url = "/search/sss?query="
search_term = "/oil+painting"


webdata = requests.get(url+search_url+search_term)
soup = BeautifulSoup(webdata.text,"html.parser")
result = soup.find("div", {"class": "content"})
# print(result.prettify())
rows = result.find_all("p", {"class": "row"})

for row in rows:
    id_url = row.find("a",{"class":"hdrlnk"})
    if id_url.get("href")[0] == "/":
        Listing_url = (url+id_url.get("href"))
    else:
        Listing_url = ("https:"+id_url.get("href"))

    title= (id_url.find("span",{"id":"titletextonly"})).text

    span = row.find("span",{"class":"price"})
    if span != None:
        price = span.text
    else:
        price = "Not listed"

    print(title,"\t",Listing_url,"\t",price)



