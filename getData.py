import requests
from bs4 import BeautifulSoup as bs

page = requests.get("http://periodictable.com/Isotopes")
print(page.status_code)

with open("index.html", "w+", encoding=page.encoding) as f:
  soup = bs(page.text, 'html.parser')
  f.write(soup.prettify())

index = []

for a in soup.find_all("a"):
  try:
    a = a.get("href")[:-1]
    b = float(a)
    index.append(a)
  except:
    print("wrong a value")

isotopes = []

for i in range(0, len(index)):
  print(str(i) + ' of ' + str(len(index)))
  page = requests.get("http://periodictable.com/Isotopes/" + index[i])
  print(page.status_code)
  soup = bs(page.text, 'html.parser')
  tables = soup.find_all('table')

  for j in range(len(tables)):
      try:
        tablesTD = tables[j].find_all('tr')[0].find_all('td')
        if "Atomic Weight" == tablesTD[0].font.string:
          print('found atomic weight')
          if tablesTD[1].string == 'N/A':
            isotopes.append([index[i], str(-1)])
          elif tablesTD[1].string != None:
            isotopes.append([index[i], tablesTD[1].string])
      except:
        pass

with open('IsotopicMass.json', 'w+') as f:
  f.write('{')
  for isotope in isotopes:
    f.write('"element' + isotope[0] +
            '" : { "AtomicMass" : ' + isotope[1] + '},')
  f.write('}')
