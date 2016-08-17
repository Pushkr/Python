import requests
import sys
from bs4 import BeautifulSoup
from requests.exceptions import ChunkedEncodingError


class GetCraiglistData:
    # default values
    url = "https://newjersey.craigslist.org/"
    s_page = "&s="
    search_url = "search/sss?&query="

    def __init__(self, search_term):
        self.search_term = search_term
        self.items = []

    def getterm(self):
        return self.search_term

    def setlocality(self, locality):
        self.url = "https://" + locality.replace(" ", "") + ".craigslist.org"
        print(self.url)

    def seturl(self, url):
        if url != 404:
            self.url = url
        else:
            print("reverting back to default url..\n")

    def __getTotalresults__(self):
        try:
            # make http request to get search result from craiglist
            webdata = requests.get(self.url + self.search_url + self.search_term)
            # use soup
            soup = BeautifulSoup(webdata.text, "html.parser")
            # find number of search items returned
            pages = soup.find("span", {"class": "button pagenum"})
        except ConnectionError as err:
            print("Error connecting site : {0}".format(err))

        if pages.text != 'no results':
            self.rangeFrom = int(pages.find("span", {"class": "rangeFrom"}).text)
            self.rangeTo = int(pages.find("span", {"class": "rangeTo"}).text)
            self.totalCount = int(pages.find("span", {"class": "totalcount"}).text)
        else:
            self.rangeFrom = 0
            self.rangeTo = 0
            self.totalCount = 0

    def printresults(self):
        self.retrievedata()
        if len(self.items) == 0:
            print("No results")
        else:
            for item in self.items:
                print(item)

    def retrievedata(self):
        self.__getTotalresults__()
        if self.totalCount == 0:
            return self.items

        rows = []
        # del soup, webdata
        print("Found %s items" % self.totalCount)

        for i in range(0, self.totalCount // 100 + 2):
            qualifiedurl = (self.url + self.search_url + self.search_term + self.s_page + str(i * 100))
            print("Fetching data from %s......" % qualifiedurl)
            try:
                webdata_full = requests.get(qualifiedurl)
                # print("web response: ", webdata_full)
                soup = BeautifulSoup(webdata_full.text, "html.parser")
                result1 = soup.find("div", {"class": "content"})
                temp_rows = result1.find_all("p", {"class": "row"})
                near_areas = (soup.find("li", {"class": "crumb area"})).find_all("option")
            except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError) as err:
                print("\n Error connecting site : {0} \n".format(err))
                return
            except ChunkedEncodingError:
                print("\n Site data delayed, skipping retrieval.. \n: {0}".format(sys.exc_info()[0]))
            finally:
                if len(temp_rows) > 0:
                    rows.append(temp_rows)

        # print(near_areas)
        # for area in near_areas:
        #     print(area['value'], area.text)

        for elements in rows:
            for row in elements:
                id_url = row.find("a", {"class": "hdrlnk"})
                # if id_url.get("href")[0] == "/":
                #     Listing_url = (self.url + id_url.get("href"))
                # else:
                lurl = ("https:" + id_url.get("href"))

                title = (id_url.find("span", {"id": "titletextonly"})).text

                span = row.find("span", {"class": "price"})
                if span is not None:
                    price = span.text
                else:
                    price = "Not listed"

                self.items.append(title + "," + lurl + "," + price)

        self.items = list(set(self.items))  # remove the duplicates.
        print("\nRetrieved %d items \n" % (len(self.items)))
        return self.items


class GetCraiglistSites:
    dict_map = {"US": 0, "CA": 1, "EU": 2, "ASIA": 3, "OCEANIA": 4, "LATAM": 5, "AF": 6}
    site_map = {}

    def __init__(self, continent="US"):
        self.continent = continent
        self.url = "https://www.craigslist.org/about/sites#" + self.continent
        self.__fetchPage__()

    def __fetchPage__(self):
        # print(self.url)
        try:
            webdata = requests.get(self.url)
            soup = BeautifulSoup(webdata.text, "html.parser")
            sites = soup.find_all("div", {"class": "colmask"})
            self.ListA = sites[self.dict_map.get(self.continent)]
            self.__extractFromList__()
        except ConnectionError as err:
            print("\nError connecting site : {0} \n".format(err))
            return
        except ChunkedEncodingError:
            print("\n Site data delayed, skipping retrieval.. : {0} \n".format(sys.exc_info()[0]))
        except:
            print("\n Unknown error : {0} \n".format(sys.exc_info()[0]))

    def __extractFromList__(self):
        anchors = self.ListA.find_all("a")
        for anchor in anchors:
            # print(anchor.text,"https:"+anchor.get("href"))
            self.site_map[anchor.text] = "https:" + anchor.get("href")

    def printall(self):
        for keys, values in self.site_map.items():
            print(keys, values)

    def getsuggestions(self, city):
        print("try these instead.. ")
        city_found = 0
        for keys, values in self.site_map.items():
            if city[:3] == keys[:3]:
                city_found = 1
                print(keys, values)
        if city_found == 0:
            print("sorry, no suggestions.")

    def forcity(self, city):
        city = city.lower()
        try:
            return self.site_map[city]
        except KeyError:
            print("\n site for city ' %s ' not found or unavailable \n" % city)
            self.getsuggestions(city)
            return 404
