import requests
import bs4

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ym_d=1628840683; _ym_uid=1628840683355101683; _ga=GA1.2.137596937.1628841988; fl=ru; hl=ru; feature_streaming_comments=true; _gid=GA1.2.1021543475.1641571984; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=599735:203282; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
    'Host': 'habr.com',
    'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
    'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36'}

KEYWORDS = {'Великобритании', '2022', 'Rust', 'Python'}
response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
hubses = []
number = 0
url_list = []
hubs_list = []
date_list = []
span_list = []
slova_list = []

# print(len(articles))
for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    #    print(number)
    hubses = ''
    for hub in hubs:
        hubses = hubses + hub.find('span').text + ' '

    hubs_list.append(hubses)
    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    span_list.append(span_title)
    # print('span - ', span_list)
    url = ('https://habr.com' + title['href'])
    if article.find('div',
                    class_='article-formatted-body article-formatted-body article-formatted-body_version-2') != None:
        slova = article.find('div',
                             class_='article-formatted-body article-formatted-body article-formatted-body_version-2').text
        slova_list.append(slova)
    else:
        slova = article.find('div',
                             class_='article-formatted-body article-formatted-body article-formatted-body_version-1').text
        slova_list.append(slova)
    date_list.append(date)
    url_list.append(url)
    number = number + 1
    print()

for ser in KEYWORDS:
    for y in range(number):
        if (ser in span_list[y]) or (ser in slova_list[y]) or (ser in hubs_list[y]):
            print(y, ser, '  _________________')
            # print('hubs-' , hubs_list[y])
            # print('slova-' , slova_list[y])
            print(date_list[y])
            print('Заголовок -', span_list[y])
            print(url_list[y])
            print()
