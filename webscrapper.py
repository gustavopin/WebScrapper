
import requests
from bs4 import BeautifulSoup
import pandas as pd


#set the URL to get the data from
url = 'http://www.vhpg.com/diablo-4-legendary-and-unique-items/'

#url requests
html = requests.get(url)

#beautufilsoup object to store the the contents of the website
soup = BeautifulSoup(html.content, 'lxml')
#print(soup.prettify())

#table of content for legendaries
table = soup.find('table', class_= "display")

#fiding more elements inside the HTML
tbody = table.find('tbody')
tr = tbody.find_all('tr')

#lists
list_name = []
list_description = []

#for function to find legendary names and store them
for element in table.find_all('a'):
    list_name.append(element.get_text())

#for function to find the description of the items
for elements in tr:
    list_temp = []
    for dl in elements.find_all('td'):
        #iterating for every line
        for li in dl.find_all('ul'):
            list_temp.append(li.text)
    list_description.append(list_temp)

#count of the elements of the list
count = 0
for element in list_name:
    count = count + 1
print(f'\nThere are {count} legendaries on this list\n')

#creating talbe in xlsx
df = pd.DataFrame({
   'Legendary Names' : list_name,
   'Legendary Description' : list_description
})

#saving a excel file
df.to_excel('legendariesD4.xlsx', sheet_name = 'Leggo Description')