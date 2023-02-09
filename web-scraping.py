from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.ole.com.ar/estadisticas/futbol/primera-division.html'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, 'html.parser')

#equipos

eq = soup.find_all('td', class_='name')

equipos = list()

count = 0
for i in eq:
    if count < 28:
        equipos.append(i.text)
    else:
        break
    count += 1

#puntos

pts = soup.find_all('td', class_='number')

puntos = list()

count = 0
for i in pts:
    if count < 28:
        puntos.append(i.text)
    else:
        break
    count += 1
    
df = pd.DataFrame({'Nombre':equipos, 'Puntos':puntos}, index=list(range(1,29)))

print(df)