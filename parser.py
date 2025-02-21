from bs4 import BeautifulSoup
import requests
import codecs


def parse():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', class_='main__content')
    description = ''
    for data in block:
        if data.find('p'):
            description = data.text
    #print(description)
    alphabet_eng = [chr(i) for i in range(65, 91)]
    alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    zapis = False
    naming = ''
    for text in str(description):
        for letter in text:
            if ((letter in alphabet_eng) or (letter in alphabet_rus)):
                zapis = True
            if (letter == '<' and zapis):
                zapis = False
                naming += '\n'
            if zapis:
                naming += letter
    file = codecs.open('save.txt', 'w', 'utf-8')
    file.write(naming)
    file.close()
