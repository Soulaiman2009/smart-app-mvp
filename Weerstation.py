def Fahrenheit(temp_Celsius):
    fahrenheit = 32 + 1.8 * temp_Celsius
    return fahrenheit

def gevoelstemperatuur(temp_Celsius, Windsnelheid, Luchtvochtigheid):
    gevoel = temp_Celsius - (Luchtvochtigheid / 100 *Windsnelheid)
    return gevoel

def weerrapport(temp_Celsius, Windsnelheid, Luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_Celsius, Windsnelheid, Luchtvochtigheid)

    if gevoel < 0 and Windsnelheid > 10:
        return 'Het is heel koud en het stormt! Verwarming helemaal aan!'
    elif gevoel < 0 and Windsnelheid <= 10:
        return 'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!'
    elif gevoel >= 0 and gevoel < 10 and Windsnelheid > 12:
        return 'Het is best koud en het waait; verwarming aan en roosters dicht!'
    elif gevoel >= 0 and gevoel < 10 and Windsnelheid <= 12:
        return 'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!'
    elif gevoel >= 10 and gevoel < 22:
        return 'Heerlijk weer, niet te koud of te warm.'
    else:
        return 'Warm! Airco aan!'

def weerstation():
    temperaturen = []
    for dag in range(7):

        Temperatuur = input('Wat is de temperatuur in graden Celsius?')
        if Temperatuur == '':
            break
        while True:
            try:
                Temperatuur = float(Temperatuur)
                break
            except ValueError:
                print('Voer een geldig getal in')
                Temperatuur = input('Wat is de temperatuur in graden Celsius?')
        temperaturen.append(Temperatuur)
        gemiddelde = sum(temperaturen) / len(temperaturen)
        while True:
            try:
                Windsnelheid = float(input('Voer de windsnelheid in, in meter per seconde?'))
                break
            except ValueError:
                print('Voer een geldig getal in')
        while True:
            try:
                Luchtvochtigheid = int(input('Wat is de luchtvochtigheid als geheel percentage 0–100?'))
                if Luchtvochtigheid >= 0 and Luchtvochtigheid <= 100:
                    break
                else:
                    print('Voer een percentage tussen 0 en 100 in.')
            except ValueError:
                print('Voer een geldig getal in')
        Graden = Fahrenheit(Temperatuur)
        rapport = weerrapport(Temperatuur, Windsnelheid, Luchtvochtigheid)
        print(Temperatuur,'°C')
        print(Graden,'°F')
        print(rapport)
        print('De gemiddelde temperatuur tot nu toe is', gemiddelde, '°C')
        print('------------------------------')

if __name__ == '__main__':
    weerstation()