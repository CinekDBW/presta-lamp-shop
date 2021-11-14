import csv
import json
import requests
from bs4 import BeautifulSoup


class Lampa:
    def __init__(self):
        self.nazwa = ""
        self.cena = 0
        self.opis = ""
        self.dane_techniczne = ""
        self.link = ""
        self.grafiki = []


def pobieranie_listy(nazwa_pliku, lista_podkategorii):
    counter = 1
    for podkategoria_indeks in range(len(lista_podkategorii)):

        lista_przedmiotow = []

        odpowiedz = requests.get(lista_podkategorii[podkategoria_indeks][1])
        soup = BeautifulSoup(odpowiedz.content, 'html.parser')

        # sprawdzenie ile jest stron z przedmiotami
        foo = soup.find_all("ul", class_="paginator")
        if len(foo) == 0:
            ile_stron = 1
        else:
            ile_stron = int(foo[0].find_all("a")[-2].text)

        for i in range(ile_stron):
            odpowiedz = requests.get(f"{lista_podkategorii[podkategoria_indeks][1]}/{i}")
            soup = BeautifulSoup(odpowiedz.content, 'html.parser')

            # wyciaganie produktow ze strony
            odpowiedz = soup.find_all(class_="prodimage f-row")

            for przedmiot in odpowiedz:
                # nazwa i link
                nazwa = przedmiot.get("title")
                link = przedmiot.get("href")
                temp = Lampa()
                temp.nazwa = nazwa
                temp.link = "https://manufakturaoswietlenia.pl" + link
                lista_przedmiotow.append(temp)

        for przedmiot in lista_przedmiotow:
            # cena
            odpowiedz = requests.get(przedmiot.link)
            soup = BeautifulSoup(odpowiedz.content, 'html.parser')
            odpowiedz = soup.find_all(class_="main-price")
            temp_cena = odpowiedz[0].text[:-3]
            temp_cena = list(temp_cena)
            for char in range(len(temp_cena)):
                if (temp_cena[char] == ','):
                    temp_cena[char] = '.'
            temp_cena = "".join(temp_cena)
            przedmiot.cena = float(temp_cena)

            # opis
            foo = soup.find_all(class_="resetcss")
            opis = ""
            for x in foo:
                opis += x.text
            przedmiot.opis = opis

            # dane techniczne
            foo = soup.find_all(class_="table")
            przedmiot.dane_techniczne = str(foo[0])

            foo = soup.find_all(class_="r--l-flex r--l-flex-vcenter")
            # print(len(foo))
            if (len(foo) == 0):
                foo = soup.find_all(class_="js__gallery-anchor-image")[0].get("href")
                przedmiot.grafiki.append("https://manufakturaoswietlenia.pl" + foo)
            else:
                for item in foo:
                    # print(item, '\n')
                    if len(item.find_all(class_="gallery js__gallery-anchor-image")) == 0:
                        item = item.find_all(class_="gallery current js__gallery-anchor-image")
                    else:
                        item = item.find_all(class_="gallery js__gallery-anchor-image")
                    przedmiot.grafiki.append("https://manufakturaoswietlenia.pl" + item[0].get("href"))

        # tutaj ostrożnie
        if (podkategoria_indeks == 0):
            copy_counter = counter
            with open(f'{nazwa_pliku}.csv', 'w', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')

                spamwriter.writerow(
                    ['ID', 'Active (0/1)', "Name *", "Categories (x,y,z...)", "Price tax included", "Quantity",
                     "Summary",
                     "Description", "Show price (0 = No, 1 = Yes)"])

                for item in lista_przedmiotow:
                    if "=" in item.nazwa:
                        item.nazwa = item.nazwa.replace("=", "-")
                    spamwriter.writerow(
                        [counter, 1, item.nazwa, lista_podkategorii[podkategoria_indeks][0], item.cena, 100, item.opis,
                         item.dane_techniczne, 1])
                    counter += 1

            with open(f'{nazwa_pliku}_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')

                spamwriter.writerow(
                    ['ID', "Image URLs (x,y,z...)"])

                for item in lista_przedmiotow:
                    grafiki = ""
                    for indeks in range(len(item.grafiki)):
                        grafiki += item.grafiki[indeks]
                        if (indeks < len(item.grafiki) - 1):
                            grafiki += ", "
                    spamwriter.writerow([copy_counter, grafiki])
                    copy_counter += 1
        else:
            copy_counter = counter
            with open(f'{nazwa_pliku}.csv', 'a', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')

                for item in lista_przedmiotow:
                    if "=" in item.nazwa:
                        item.nazwa = item.nazwa.replace("=", "-")
                    spamwriter.writerow(
                        [counter, 1, item.nazwa, lista_podkategorii[podkategoria_indeks][0], item.cena, 100, item.opis,
                         item.dane_techniczne, 1])
                    counter += 1
            with open(f'{nazwa_pliku}_urls.csv', 'a', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';')

                for item in lista_przedmiotow:
                    grafiki = ""
                    for indeks in range(len(item.grafiki)):
                        grafiki += item.grafiki[indeks]
                        if (indeks < len(item.grafiki) - 1):
                            grafiki += ", "
                    spamwriter.writerow(
                        [copy_counter, grafiki])
                    copy_counter += 1
        print(f"{lista_podkategorii[podkategoria_indeks][0]} done")


lista_podkategorii = [(11, "https://manufakturaoswietlenia.pl/pl/c/Drewniane/83"),
                      (12, "https://manufakturaoswietlenia.pl/pl/c/Metalowe/84"),
                      (21, "https://manufakturaoswietlenia.pl/pl/c/1-plomienne/77"),
                      (22, "https://manufakturaoswietlenia.pl/pl/c/2-plomienne/78"),
                      (23, "https://manufakturaoswietlenia.pl/pl/c/3-plomienne/79"),
                      (24, "https://manufakturaoswietlenia.pl/pl/c/4-plomienne/88"),
                      (25, "https://manufakturaoswietlenia.pl/pl/c/5-plomienne/89"),
                      (26, "https://manufakturaoswietlenia.pl/pl/c/6-plomienne/90"),
                      (27, "https://manufakturaoswietlenia.pl/pl/c/8-plomienne/97"),
                      (28, "https://manufakturaoswietlenia.pl/pl/c/12-plomienne/98"),
                      (31, "https://manufakturaoswietlenia.pl/pl/c/1-plomienne/80"),
                      (32, "https://manufakturaoswietlenia.pl/pl/c/2-plomienne/81"),
                      (33, "https://manufakturaoswietlenia.pl/pl/c/3-plomienne/82"),
                      (40, "https://manufakturaoswietlenia.pl/pl/c/Kinkiety/72"),
                      (50, "https://manufakturaoswietlenia.pl/pl/c/Lampki-nocne-i-biurkowe/69"),
                      (60, "https://manufakturaoswietlenia.pl/pl/c/Lampy-dla-dzieci/73"),
                      (70, "https://manufakturaoswietlenia.pl/pl/c/Zarowki/71"),
                      (80, "https://manufakturaoswietlenia.pl/pl/new")
                      # (90,"https://manufakturaoswietlenia.pl/pl/promotions")
                      ]

pobieranie_listy("produkty", lista_podkategorii)
#pobieranie_listy("debug", [(27, "https://manufakturaoswietlenia.pl/pl/c/8-plomienne/97")])

print("program ended")
