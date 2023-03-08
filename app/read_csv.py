import csv

def read_csv(path):
    #Con esta orden se abre el archivo en modo lectura y se cierra automaticamente al terminar
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #Se crea un diccionario con la informacion recibida
        #sacamos el encabezado usando iterable
        header = next(reader)
        #Creamos una lista vacia donde despues se guardara la informacion 
        data = []
        for row in reader:
            #Unimos el header con su informacion usando zip
            iterable = zip(header, row)
            #Creamos un dccionario con las clave valor del iterable y lo guardamos en la lista data
            #Usando dictyonary comprehension se hace la transformacion 
            country_dict = {key : value for key, value in iterable}
            #Se adiciona cada diccionario a la lista data
            data.append(country_dict)
        return data


if __name__=='__main__':
    data = read_csv('./app/data.csv')
    print(data[0])            