from bs4 import BeautifulSoup
import requests


#set the URL to get the data from
url = requests.get('https://www.kabum.com.br/hardware/placa-de-video-vga')

#class="sc-1fc62739-12 hJsABb" - main class on the site that have the lists
#class="sc-ff8a9791-7 hDHAaY productCard" - class for each individual product