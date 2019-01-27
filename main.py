import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME = 'tamiltunes'
HOMEPAGE = 'http://tamiltunes.pro/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# creating the threads.

def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t  = threading.Thread(target=work)
        t.daemon = True
        t.start()

# what work the thread should do
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()


def createJobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# crawl item in queue
def crawl():
    queuedLinks = file_to_set(QUEUE_FILE)
    if len(queuedLinks) > 0:
        print(str(len(queuedLinks)) + ' links in queue')
        createJobs()


createWorkers()
crawl()