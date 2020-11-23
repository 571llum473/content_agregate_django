from django.core.management.base import BaseCommand
from get_cntnt.models import Source, News
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    help = "scrape news"
    def handle(self, *args, **options):
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
                try:
                    snippet = tag.description.text.lstrip()
                    if snippet.startswith("<"):
                        parse_html = BeautifulSoup(snippet, 'html.parser')
                        snippet = parse_html.text
                except:
                    snippet = False
                try:
                    source_object.news_set.create(
                        news_text=news_text, 
                        pub_time=pub_time, 
                        snippet=snippet, 
                        rss=rss)
                    print('%s added' % (news_text,))
                except: 
                    print('%s already exists' % (news_text,))
        self.stdout.write('scrape complete')