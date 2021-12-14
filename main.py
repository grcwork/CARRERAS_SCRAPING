import requests
from bs4 import BeautifulSoup
import csv
import os

# Traer la ágina
r = requests.get("https://www.ucentral.cl/carreras-profesionales")

# Crear la sopa o árbol
soup = BeautifulSoup(r.text, 'lxml')

# Referenciar los datos
raw_data = soup.find('div', class_='CUERPO')

data = []
for item in raw_data.contents:

    if item.name == 'p':
        child_items = item.find('a')
        if child_items != None and child_items['name'] == "coquimbo":
            break

    if item.name == "ul":
        for li in item.contents:
            if li.text != "\n":
                data.append([li.text])

if __name__ == '__main__':
    # Crear directorio para guardar los datos extraídos
    if not os.path.isdir("data"):
        os.mkdir("data")
    
    # Guardamos las carreras encontrados
    with open('data/carreras.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # Guardar header
        writer.writerow(['Carrera'])

        # Guardar carreras encontrados        
        writer.writerows(data)