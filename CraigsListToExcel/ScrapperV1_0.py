import requests
from bs4 import BeautifulSoup


class getCraiglistData:
    url = "https://newjersey.craigslist.org/"
    s_page ="&s="
    search_url = "search/sss?&query="

    def __init__(self,search_term):
        self.search_term = search_term

    def getTerm(self):
        return self.search_term

    def setlocality(self,locality):
        self.url = "https://"+ locality.replace(" ","")+".craigslist.org"
        print(self.url)

    def setURL(self,url):
        if url != 404:
            self.url = url
        else:
            print("reverting back to default url..")


    def __getTotalresults__(self):
         # make http request to get search result from craiglist
        webdata = requests.get(self.url + self.search_url + self.search_term)
        # use soup
        soup = BeautifulSoup(webdata.text, "html.parser")
        # find number of search items returned
        pages = soup.find("span", {"class": "button pagenum"})
        if pages.text != 'no results':
            self.rangeFrom = int(pages.find("span", {"class": "rangeFrom"}).text)
            self.rangeTo = int(pages.find("span", {"class": "rangeTo"}).text)
            self.totalCount = int(pages.find("span", {"class": "totalcount"}).text)
        else:
            self.rangeFrom = 0
            self.rangeTo = 0
            self.totalCount = 0


    def printResults(self):
        self.retrieveData()
        if len(self.items) ==0:
            print("No results")
        else:
            for item in self.items:
                print(item)


    def retrieveData(self):
        self.__getTotalresults__()
        self.items = []
        if self.totalCount == 0:
            return self.items

        rows = []
        # del soup, webdata
        print("Found %s items" %self.totalCount)
        for i in range(0, self.totalCount // 100 + 2):
            qualifiedURL = (self.url + self.search_url + self.search_term + self.s_page + str(i * 100))
            print("Fetching data from %s......" %qualifiedURL)
            webdata_full = requests.get(qualifiedURL)
            soup = BeautifulSoup(webdata_full.text, "html.parser")
            result1 = soup.find("div", {"class": "content"})
            temp_rows = result1.find_all("p", {"class": "row"})
            if len(temp_rows) > 0:
                rows.append(temp_rows)

        for elements in rows:
            for row in elements:
                id_url = row.find("a", {"class": "hdrlnk"})
                # if id_url.get("href")[0] == "/":
                #     Listing_url = (self.url + id_url.get("href"))
                # else:
                Listing_url = ("https:" + id_url.get("href"))

                title = (id_url.find("span", {"id": "titletextonly"})).text

                span = row.find("span", {"class": "price"})
                if span is not None:
                    price = span.text
                else:
                    price = "Not listed"

                self.items.append(title + "," + Listing_url + "," + price)

        self.items = list(set(self.items))   # remove the duplicates.
        return self.items


class getCraiglistSites:
    dict_map = {"US":0,"CA":1,"EU":2,"ASIA":3,"OCEANIA":4,"LATAM":5,"AF":6}
    site_map = {}

    def __init__(self,continent = "US"):
        self.continent = continent
        self.url = "https://www.craigslist.org/about/sites#"+self.continent
        self.__fetchPage__()

    def __fetchPage__(self):
        # print(self.url)
        webdata = requests.get(self.url)
        # use soup
        soup = BeautifulSoup(webdata.text, "html.parser")
        sites = soup.find_all("div",{"class":"colmask"})
        # data = soup.find("h1")
        self.ListA = sites[self.dict_map.get(self.continent)]
        self.__extractFromList__()

    def __extractFromList__(self):
        anchors = self.ListA.find_all("a")
        for anchor in anchors:
            # print(anchor.text,"https:"+anchor.get("href"))
            self.site_map[anchor.text] = "https:"+anchor.get("href")

    def printAll(self):
        for keys,values in self.site_map.items():
            print(keys,values)

    def forCity(self,city):
        city = city.replace(" ","").lower()
        try:
            return self.site_map[city]
        except KeyError:
            print("site for city ' %s ' not found or unavailable" %city)
            return 404

# s1 = getCraiglistData("oil+painting")
# s1.setlocality("newyork")
# results = s1.retrieveData()

# for record in results:
#     print(record)


g1 = getCraiglistData("sex")
g1.setURL(getCraiglistSites().forCity('albany'))
g1.printResults()


