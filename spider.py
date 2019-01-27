from urllib.request import Request, urlopen
from linkFinder import LinkFinder
from general import *

class Spider:

    # global variables
    projectName = ''
    baseURL = ''
    domainName = ''
    queuedFile = ''
    crawledFile = ''
    mp3File = ''
    queue = set()
    crawled = set()
    mp3 = {}

    def __init__(self, projectName, baseURL, domainName):
        Spider.projectName = projectName
        Spider.baseURL = baseURL
        Spider.domainName = domainName
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        Spider.queuedFile = Spider.projectName + '/queue.txt'
        Spider.mp3File = Spider.projectName + '/mp3List.txt'
        self.boot()
        self.crawlPage('First Spider', Spider.baseURL)

    @staticmethod
    def boot():
        create_project_dir(Spider.projectName)
        create_files(Spider.projectName, Spider.baseURL)
        Spider.queue = file_to_set(Spider.queuedFile)
        Spider.crawled = file_to_set(Spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, pageURL):
        if pageURL not in Spider.crawled:
            print(threadName +  'now crawling ' + pageURL)
            print('Queued ' + str(len(Spider.queue)) + ' Crawled ' + str(len(Spider.crawled)))
            Spider.addLinksToQueue(Spider.gatherLinks(pageURL))
            Spider.queue.remove(pageURL)
            Spider.crawled.add(pageURL)
            Spider.updateFiles()

    @staticmethod
    def gatherLinks(pageURL):
        htmlString = ''
        hdr = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = Request(pageURL, headers=hdr)
            page = urlopen(response)
            # if response.getheader('content-Type') == 'text/html':
            htmlBytes = page.read()
            htmlString = htmlBytes.decode("utf-8")
            finder = LinkFinder(Spider.baseURL, pageURL)
            finder.feed(htmlString)
        except:
            print('Error Parsing page :' + pageURL)
            return set()
        return finder.pageLinks()

    @staticmethod
    def addLinksToQueue(*links):
        print(links)
        mp3links = {}
        if links[0]:
            linkset = links[0]
            links = linkset[0]
            mp3links = linkset[1]
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainName not in url:
                continue
            Spider.queue.add(url)
        Spider.mp3 = mp3links.copy()

    @staticmethod
    def updateFiles():
        set_to_file(Spider.queue, Spider.queuedFile)
        set_to_file(Spider.crawled, Spider.crawledFile)
        mp3_to_file(Spider.mp3, Spider.mp3File)
