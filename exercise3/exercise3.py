# I Love Big Data <3
import csv
import json


def display_result(result):
    for region in result.keys():
        print(region + ': ')
        for prezydent in result['polska'].keys():

            print(region + ' => ' + ' ' + prezydent + " = " + str(result[region][prezydent]) + " głosów")


result = {
'polska': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'dolnośląskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'kujawsko-pomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'lubelskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'lubuskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'łódzkie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'małopolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'mazowieckie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'opolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'podkarpackie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'podlaskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'pomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'śląskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'świętokrzyskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'warmińsko-mazurskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'wielkopolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
'zachodniopomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0, 'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
}
with open('prezydent_2015_tura1.csv', 'r', encoding='ANSI') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')

    for row in csvreader:
        for prezydenci in result['polska'].keys():
            result['polska'][prezydenci] += int(row[prezydenci])
            result[row['Województwo']][prezydenci] += int(row[prezydenci])

display_result(result)

with open('result.json', 'w') as jsonfile:
    json.dump(result, jsonfile)