import os

personName = input("Ingrese su nombre: ")
dataPath = 'Data'
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)
    count = 0
else:
    count = len(os.listdir(personPath))
    print(f'Carpeta contiene {count} fotos, se agregaran nuevas')
