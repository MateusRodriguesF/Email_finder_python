import requests
import re

to_crawl = ['http://exemplo.com']
crawled = set()

emails_found = set()

header = {'user-agent': 
                        'Mozilla/5.0 (X11; Linux x86_64; rv:68.0)'
                        ' Gecko/20100101 Firefox/68.0'}


for i in range(15):
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print 'Crawling:', url

    emails = re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)

    for email in emails:
        emails_found.add(email)

print emails_found
