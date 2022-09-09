import bs4
import requests
from fake_http_header import FakeHttpHeader
from pprint import pprint

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'производители', 'России']

    fake_header = FakeHttpHeader()

    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    fake_header_dict = fake_header.as_header_dict()
    response = requests.get(url, headers=fake_header_dict)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')

    articles = soup.find_all(class_='tm-articles-list__item')
    for article in articles:
        h2_class = article.find(class_='tm-article-snippet__title-link')
        href = h2_class.attrs['href']
        link = base_url + href
        title = h2_class.find('span')
        title = [i.text.strip() for i in title]
        meta = article.find(class_='tm-article-snippet__meta')
        data_time = meta.find('time')
        data_time = [i.text.strip() for i in data_time]

        text = article.find(class_='tm-article-body tm-article-snippet__lead').text
        text_split = text.split(" ")
        for item in text_split:
            for i in KEYWORDS:
                if i == item:
                    print(data_time[0])
                    print(title[0])
                    print(link)
