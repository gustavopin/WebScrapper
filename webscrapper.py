import requests
from bs4 import BeautifulSoup

#set the URL to get the data from
url = 'http://www.vhpg.com/diablo-4-legendary-and-unique-items/'

#url requests
html = requests.get(url)

#beautufilsoup object
soup = BeautifulSoup(html.content, 'html.parser')

#getting the information from the interested "body" of the html
database = soup.find(id="vhpg")
print(database.prettify())

#finding the elements by class TBI
#legendaries = database.find_all('div', class_="dataTables_wrapper no-footer")
#print(legendaries.prettify())

#for function to create the sequence TBI
#for legendary in legendaries:
    #name = legendary.find('a', class_="Legendary Name: ")
    #print(name)