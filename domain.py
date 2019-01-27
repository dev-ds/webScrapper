from urllib.parse import urlparse

# return the xxxx.com alone from the entire name
def getDomainName(url):
    try:
        result = getSubDomainName(url).split('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''

# get the domain name, the xxxx.com so that no matter how the url is
# we get the correct domain name
def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''