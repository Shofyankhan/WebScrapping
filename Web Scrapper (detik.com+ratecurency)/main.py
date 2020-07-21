import bs4
from pip._vendor.requests import get

html_doc = get('https://detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')

popular_area = soup.find(attrs={'class':'grid-row list-content'})

titles = popular_area.find_all(attrs={'class':'media__title'})

images = popular_area.find_all(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

#print(titles)

