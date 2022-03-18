import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key= lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
    hn = []
    for link, subtext in zip(links, subtexts):
        title = link.getText()
        href = link.get('href', None)
        vote = subtext.select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

def most_rated_news(num_pages):
    hn = []
    for i in range(1,num_pages+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
        soup_object = BeautifulSoup(res.text, 'html.parser')
        links = soup_object.select('.titlelink')
        subtext = soup_object.select('.subtext')
        hn += create_custom_hn(links, subtext)
    return sort_stories_by_votes(hn)

pprint.pprint(most_rated_news(2))