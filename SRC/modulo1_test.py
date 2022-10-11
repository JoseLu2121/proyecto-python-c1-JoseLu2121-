from modulo1 import *

def mostrardatos(fichero):
    '''
    Esta función cuya entrada es la URL relativa del dataset imprimimos el número total de registros leídos además de los tres primeros y los
    tres últimos.
    
    @param fichero: Ruta del archivo csv
    @type fichero: str

    '''
    
    listatotal=abrirdatos(fichero)
    print('='*100)
    print('Total de registros: '+str(len(listatotal)))
    print('='*100+'\n')
    print('='*100)
    print('Primeros 3 registros')
    for d in listatotal[:3]:
        print(d)
    print('='*100)
    print('\n'+'='*100)
    print('Últimos 3 registros')
    for d in listatotal[-3:]:
        print(d)
    print('='*100)
    
    pass

def main():
    mostrardatos(".\proyecto-python-c1-JoseLu2121\Data\dataset1.csv")
    
if __name__ == '__main__':
    main()
    
