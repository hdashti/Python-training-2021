import urllib.request
import re


class Website:
    def __init__(self, url):
        self.__url = url
        self.__text = ""

    @property
    def url(self):
        return self.__url

    @property
    def text(self):
        if self.__text == "":
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')
        return self.__text

    @property
    def links(self):
        urls = re.findall(r'href="(https?://.+?)"', self.text)
        return [Website(url) for url in urls]

    def __repr__(self):
        return f"WEBSITE[{self.url}]"




url = "https://python.org"

# open website
website = Website(url)

# print the website texts
#print(website.get_text())
text = website.text


# list the websites in the website
list_of_websites = website.links


# show the text of the fifth website
print(list_of_websites[5].text)

print(list_of_websites)

