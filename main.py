import Weerstation
import smart_app_controller
import json
from urllib.request import urlopen
from urllib.error import URLError

def huidig_weer():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current=temperature_2m"

    try:
        with urlopen(url, timeout=10) as antwoord:
            gegevens = json.loads(antwoord.read().decode('utf-8'))

            temperatuur = gegevens['current']['temperature_2m']
            eenheid = gegevens['current_units']['temperature_2m']
            print(f'\nDe huidige temperatuur in Utrecht is {temperatuur} {eenheid}.')

    except(URLError, TimeoutError, KeyError, ValueError,) as fout:
        print('Het ophalen van het weer is niet gelukt.')
        print('fout', fout)

def hoofdmenu():
    while True:
        print('\n=====================================')
        print('         Smart App Platform ')
        print('=====================================')
        print('1. Weerstation')
        print('2. Smart App Controller')
        print('3. Huidig weer ophalen.')
        print('4. Afsluiten')

        keuze = input('Voer het getal van de keuze in').strip()

        if keuze == '1':
            Weerstation.weerstation()
        elif keuze == '2':
            smart_app_controller.smart_app_controller()
        elif keuze == '3':
            huidig_weer()
        elif keuze == '4':
            print('Tot ziens!')
            break
        else:
            print('Ongeldige keuze. Kies 1, 2, 3 of 4.')

if __name__ == '__main__':
    hoofdmenu()