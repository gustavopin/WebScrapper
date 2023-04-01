import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


#set the URL to get the data from
url = 'http://www.vhpg.com/diablo-4-legendary-and-unique-items/'

#url requests
html = requests.get(url)

#beautufilsoup object to store the the contents of the website
soup = BeautifulSoup(html.content, 'lxml')
#print(soup.prettify())

#table of content for legendaries
table = soup.find('table', class_= "display")

#list for the names
list_name = []
list_description = []

#for function to find legendary names and store them
for element in table.find_all('a'):
    list_name.append(element.get_text())
    for subelements in table.find_all('ul'):
        list_description.append(subelements.get_text())
print(list_name)
print(list_description)

#list for legendary description
#list_description = []

#for function to find legendary description
#for element in table:
    #list_description.append(element.get_text())
#print(list_description)

count = 0
#count of the elements of the list
for element in list_name[0]:
    count = count + 1
print(f'\nThere are {count} legendaries on this list\n')

#creating talbe in xlsx
df = pd.DataFrame({
   'Legendary Names' : list_name,
   'Legendary Description' : list_description
})

#saving a excel file
df.to_excel('legendariesD4.xlsx', sheet_name = 'Leggo Description')