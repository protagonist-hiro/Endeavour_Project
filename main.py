import RAKE
import ParseRss
def main():
    a=input('sdfsdfsd')
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    url='http://www.dailynews.com/section?template=RSS&profile=4000036&mime=xml'
    news=ParseRss.newsFromLink(url,headers)
    keywords = RAKE.rakeTheText(news[0].get_description(),'RAKE/SmartStoplist.txt')
    print(news[0].get_description())
    print(news[0].get_category())
    print(keywords)

if __name__=='__main__':
    main()
