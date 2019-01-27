from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def error(self, message):
        pass
    def __init__(self, baseURL, pageURL):
        super().__init__()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set()
        self.mp3 = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            print(attrs)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'title':
                    songtitle = value
                if attribute == 'href':
                    url = parse.urljoin(self.baseURL, value)
                    if str(url).split('.')[-1] == 'mp3':
                        self.mp3[songtitle] = url
                    else:
                        self.links.add(url)
    def pageLinks(self):
        return (self.links, self.mp3)