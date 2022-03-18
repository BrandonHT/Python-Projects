import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup_object = BeautifulSoup(res.text, 'html.parser')
links = soup_object.select('.titlelink')
votes = soup_object.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for link, vote in zip(links, votes):
        title = link.getText()
        href = link.get('href', None)
        points = int(vote.getText().replace(' points', ''))
        hn.append({'title': title, 'link': href})
    return hn


hn = create_custom_hn(links, votes)