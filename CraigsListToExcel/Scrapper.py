import requests
from bs4 import BeautifulSoup

url = "https://newjersey.craigslist.org"
search_url = "/search/sss?query="
search_term = "honda"
s_page = "&s="

# make http request to get search result from craiglist
webdata = requests.get(url + search_url + search_term)
# use soup
soup = BeautifulSoup(webdata.text, "html.parser")

rows = []

# #find first page of search result in soup
# result = soup.find("div", {"class": "content"})
# rows = result.find_all("p", {"class": "row"})

# find number of search items returned
pages = soup.find("span", {"class": "button pagenum"})
rangeFrom = int(pages.find("span", {"class": "rangeFrom"}).text)
rangeTo = int(pages.find("span", {"class": "rangeTo"}).text)
totalCount = int(pages.find("span", {"class": "totalcount"}).text)
# print(rangeFrom,rangeTo,totalCount)

del soup, webdata
print("Found %s items" % totalCount)
for i in range(0, totalCount // 100 + 2):
    print("Fetching data from %s......" % (url + search_url + search_term + s_page + str(i * 100)))
    webdata_full = requests.get(url + search_url + search_term + s_page + str(i * 100))
    soup = BeautifulSoup(webdata_full.text, "html.parser")
    result1 = soup.find("div", {"class": "content"})
    temp_rows = result1.find_all("p", {"class": "row"})
    if len(temp_rows) > 0:
        rows.append(temp_rows)

items = []
for elements in rows:
    for row in elements:
        id_url = row.find("a", {"class": "hdrlnk"})
        if id_url.get("href")[0] == "/":
            Listing_url = (url + id_url.get("href"))
        else:
            Listing_url = ("https:" + id_url.get("href"))

        title = (id_url.find("span", {"id": "titletextonly"})).text

        span = row.find("span", {"class": "price"})
        if span is not None:
            price = span.text
        else:
            price = "Not listed"

        items.append(title + "\t" + Listing_url + "\t" + price)

items = list(set(items))   # remove the duplicates.

for item in items:
    print(item)
