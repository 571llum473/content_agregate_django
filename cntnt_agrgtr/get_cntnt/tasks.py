from bs4 import BeautifulSoup
from get_cntnt.models import Source
import requests
from cntnt_agrgtr.celery import app

@app.task
def scrape():
    for source_name in Source.objects.all():
        source_object = Source.objects.get(name=source_name)
        news_url = source_object.rss
        r = requests.get(news_url)
        soup = BeautifulSoup(r.content, 'xml')
        items = soup.find_all("item", limit=5)

        for tag in items:
            rss = tag.link.text
            news_text = tag.title.text
            pub_time = tag.pubDate.text.split(' ')[-2]
            snippet = tag.description.text
            try:
                source_object.news_set.create(
                    news_text=news_text, 
                    pub_time=pub_time, 
                    snippet=snippet, 
                    rss=rss)
                print('%s added' % (news_text,))
            except: 
                print('%s already exists' % (news_text,))
        