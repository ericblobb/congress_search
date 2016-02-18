from bs4 import BeautifulSoup
import magic
import urllib
import os
import mechanize
import Cookie
import cookielib

cookiejar = cookielib.LWPCookieJar()
br = mechanize.Browser()
br.set_cookiejar(cookiejar)
br.set_handle_robots(False)
br.addheaders = [("User-agent", "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; T312461)")]

search = ""

while True:
    search = str(raw_input("\nEnter your search: "))

    if search is "q":
        break

    search_plus = search.replace(" ", "+")

    search_percent = search.replace(" ", "%20")

    print "\nYou searched: " + search + "\n"

    data = br.open("https://cse.google.com/cse?cx=015560548092242357066%3Awb9hyhrlxms&ie=UTF-8&q={0}&sa=Search#gsc.tab=0&gsc.q={1}&gsc.page=1".format(search_plus, search_percent)).read()

    parsed = BeautifulSoup(data, "html.parser")

    num = 0

    os.mkdir(search)

    for i in parsed.findAll('a'):
        if num > 0 and num < 11:
            print "Downloading file: " + str(num) + "..."
            title = i.get_text()
            filename = search + "/" + title
            #urllib.urlretrieve(i.get("href"), filename)
            try:
                contents = br.open(i.get("href")).read()
            except:
                continue
            my_file = open(filename, "w")
            my_file.write(contents)
            my_file.close()
            if "HTML" in magic.from_file(filename):
                os.rename(filename, filename + ".html")
            elif "PDF" in magic.from_file(filename):
                os.rename(filename, filename + ".pdf")
            elif "PostScript" in magic.from_file(filename):
                os.rename(filename, filename + ".ps")
        num += 1

    print "\nDownload complete\n"
print "Exiting..."
