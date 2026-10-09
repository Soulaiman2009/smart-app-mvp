def aantal_dagen(inputFile):
    try:
        with open(inputFile, 'r') as bestand:
            regels = bestand.readlines()
            dagen = len(regels) - 1
            return dagen
    except FileNotFoundError:
        print('Fout: het bestand', inputFile, 'is niet gevonden.')
        return -1
    except OSError:
        print('Fout: het bestand kon niet worden geopend')
        return -1

def auto_bereken(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as bestand:
            regels = bestand.readlines()
    except OSError:
        print('Fout: het invoerbestand kon niet worden geopend.')
        return False

    uitvoerregels = []

    try:
        for regel in regels[1:]:
            gegevens = regel.split()

            datum = gegevens[0]
            numPeople = int(gegevens[1])
            tempSetpoint = float(gegevens[2])
            tempOutside = float(gegevens[3])
            precip = float(gegevens[4])

            verschil = tempSetpoint - tempOutside

            if verschil >= 20:
                CV = 100
            elif verschil >= 10:
                CV = 50
            else:
                CV = 0

            ventilatie = numPeople + 1
            if ventilatie > 4:
                ventilatie = 4

            if precip < 3:
                bewatering = True
            else:
                bewatering = False

            uitvoerregels.append(
                datum + ';' + str(CV) + ';' + str(ventilatie)
                + ';' + str(bewatering) + '\n'
            )

    except (ValueError, IndexError):
        print('Fout: er staan ongeldige gegevens in het invoerbestand.')
        return False

    try:
        with open(outputFile, 'w') as uitvoerbestand:
            uitvoerbestand.writelines(uitvoerregels)
    except OSError:
        print('Fout: het uitvoerbestand kon niet worden opgeslagen.')
        return False

    return True

def overwrite_settings(outputFile):
    datum = input('Welke datum wil je aanpassen?').strip()
    try:
        with open(outputFile, 'r') as bestand:
            regels = bestand.readlines()
    except OSError:
        print('Fout: het uitvoerbestand kon niet worden geopend.')
        return False

    datum_gevonden = False

    for regel in regels:
        gegevens = regel.strip().split(';')

        if gegevens[0] ==datum:
            datum_gevonden = True
            print('Datum gevonden!')
            systeem = input('Welk systeem wil je aanpassen? 1 = CV, 2 = Ventilatie, 3 = Bewatering:')
            if systeem not in ['1', '2', '3']:
                return -3
            if systeem == '1':
                try:
                    nieuwe_waarde = int(input('Welke nieuwe CV waarde wil je instellen?'))
                except ValueError:
                    return -3
                if nieuwe_waarde >= 0 and nieuwe_waarde <= 100:
                    gegevens[1] = str(nieuwe_waarde)
                    regels[regels.index(regel)] = ';'.join(gegevens) + '\n'
                    print('Geldige CV waarde!')
                else:
                    print('Ongeldige waarde!')
                    return -3
            if systeem == '2':
                try:
                    nieuwe_waarde = int(input('Welke nieuwe ventilatiewaarde wil je instellen?'))
                except ValueError:
                    return -3
                if nieuwe_waarde < 0 or nieuwe_waarde > 4:
                    print('Ongeldige ventilatiewaarde!')
                    return -3
                else:
                    gegevens[2] = str(nieuwe_waarde)
                    regels[regels.index(regel)] = ';'.join(gegevens) + '\n'
                    print('Ventilatiewaarde aangepast!')
            if systeem == '3':
                nieuwe_waarde = input('Bewatering aan(1) of uit(0)?')
                if nieuwe_waarde == '0':
                    gegevens[3] = 'False'
                elif nieuwe_waarde == '1':
                    gegevens[3] = 'True'
                else:
                    print('Ongeldige bewateringwaarde!')
                    return -3
                regels[regels.index(regel)] = ';'.join(gegevens) + '\n'
                print('bewatering aangepast!')
    if datum_gevonden == False:
        return -1
    try:
        with open(outputFile, 'w') as bestand:
            for regel in regels:
                bestand.write(regel)
    except OSError:
        print('Fout: de wijzigingen konden niet worden opgeslagen.')
        return -1

    return 0

def smart_app_controller():
    while True:
        print('\n-----------------------')
        print('Welkom bij de Smart App Controller!')
        print('1. aantal dagen tonen.')
        print('2. Instellingen automatisch berekenen.')
        print('3. Een instelling aanpassen.')
        print('4. Stoppen')
        print('-----------------------')
        keuze = input('Voer het getal van de keuze in').strip()

        if keuze == '1':
            print('\nAantal dagen:',aantal_dagen('input.txt'))
        elif keuze == '2':
            resultaat = auto_bereken('input.txt', 'output.txt')
            if resultaat:
                print('\nInstellingen zijn berekend.')
        elif keuze == '3':
            resultaat = overwrite_settings('output.txt')
            print('Resultaatcode:', resultaat)
        elif keuze == '4':
            print('\nTot ziens!')
            break
        else:
            print('\nOngeldige keuze. Kies 1, 2, 3 of 4.')

        input('\nDruk op Enter om verder te gaan...')

if __name__ == '__main__':
    smart_app_controller()