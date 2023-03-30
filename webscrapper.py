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
for element in table:
    list_name.append(table.find_all('a'))
for a in list_name[0]:
    print(a)

count = 0
#count of the elements of the list
for x in list_name[0]:
    count = count + 1
print(f'\nThere are {count} elements in this list')

#list_name = [table.find_all('a') for i in table][0] 
#for i in list_name:
#print(i)
#list comprehension for the funcion above