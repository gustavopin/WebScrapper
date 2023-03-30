import requests
from bs4 import BeautifulSoup


#set the URL to get the data from
url = 'http://www.vhpg.com/diablo-4-legendary-and-unique-items/'

#url requests
html = requests.get(url)

#beautufilsoup object to store the the contents of the website
soup = BeautifulSoup(html.content, 'html.parser')
#print(soup.prettify())

#table of content for legendaries
table = soup.find('table', class_= "display")

#remove the # of this print in case you want to see all the html elements inside the table
#print(table.prettify())

#list for the names
list_name = []

#for function to find legendary names
for elements in table:
    name = table.find_all('a')
    list_name.append(name)
    print(list_name)
