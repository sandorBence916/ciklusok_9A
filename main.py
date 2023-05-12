import pandas as pd

if __name__ == '__main__':
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    ##print(diamonds)

    ##print(diamonds['carat'])

    sum = 0
    for i in diamonds['carat']:
        sum += i
    print('karát összesen: ' + str(sum))

    darabszam = diamonds['carat'].count()
    print('darabszám: '+ str(darabszam))


    atlag = sum / darabszam
    print('átlag: ' + str(atlag))

    for gyemant in diamonds.iterrows():
        carat = gyemant [1]['carat']
        if carat > atlag:
            #print(gyemant)
            pass


    for gyemant in diamonds.iterrows():
        color = gyemant[1]['color']
        if color == 'H':
            #print(gyemant)
            pass
        price = gyemant[1]['price']

    szum = 0
    for gyemant in diamonds.iterrows():
        price = gyemant[1]['price']
        color = gyemant[1]['color']
        if color == 'H':
            szum += price


    print("price: " + str(szum))

    # Ha gyémánt színe 'H'
        # akkor adjuk össze a price oszloból az értékeket
