from Scrapper import GetCraiglistSites, GetCraiglistData

try:

    s1 = GetCraiglistData((input("Enter search item").replace(" ", "+")))
    s1.seturl(GetCraiglistSites().forcity("albany"))
    s1.printresults()
except ConnectionError:
    print("Error retrieving data from site")
