
import urllib.request
import bs4 as bs
import re
#extract from sitemaps from a news website
#constantly track sitemaps for bots

#Websites will not give you sitemaps if you are doing it programmatically
#so we create a user agent to fake the websites
class News:

    def __init__(self,url):
        self.guid= url.find('guid').text
        self.link=url.find('link').text
        self.desc=url.find('description').text
        self.pub_date=url.find('pubDate').text
        self.title=url.find('title').text
        self.update_date=url.find('updateDate').text
        self.override_url=url.find('overrideUrl').text
        self.category=[category.text for category in url.find_all('category')]

    def get_category(self):
        return self.category

    def get_title(self):
        return self.title

    def get_description(self):
        return re.sub('(\<.*?\>)','',self.desc)



def newsFromLink(url,headers):
    req = urllib.request.Request(url,headers=headers)
    sauce=urllib.request.urlopen(req).read()
    soup=bs.BeautifulSoup(sauce,'xml')
    news=[]

    for item in soup.find_all('item'):
        news.append(News(item))
    return news
