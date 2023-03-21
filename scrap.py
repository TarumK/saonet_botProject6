import requests
from bs4 import BeautifulSoup as bs
# wordRus = input('Введите слово для перевода: ')

def translate(wordRus):
    URL_TEMPLATE = f'https://translate.academic.ru/{wordRus}/ke/ru/'
# URL_TEMPLATE = "https://translate.academic.ru/молоко/ke/ru/"
    r = requests.get(URL_TEMPLATE)
# print(r.status_code)
# print(r.text)
    soup = bs(r.text, "html.parser")
# WordsOfTranslate = soup.find_all('span', class_='item')
    WordsOfTranslate = soup.find_all('strong',)
    try:
        wordCir = (WordsOfTranslate[2].text)
    except IndexError:
        wordCir = 'Термин, отвечающий запросу, не найден.'
    # print(WordsOfTranslate[2].text)
    return wordCir

# for word in WordsOfTranslate:
#     print(word.text)
# <span class="num0 user_selection_true">дагъэ<span class="closewrap">
# <p>
# 				<span class="item">1</span>
# 				<strong>дагъэ</strong>
# 							</p>
