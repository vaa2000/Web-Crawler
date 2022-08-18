import requests
from bs4 import BeautifulSoup

url="https://collegedunia.com/canada/computer-science-and-engineering-colleges"

#1
r = requests.get(url)
htmlContent = r.content

#2
soup=BeautifulSoup(htmlContent,'html.parser')

#3
item=soup.find_all("a",class_="cd-nav-dropdown-sub-heads")

for i in item:
    print(i.get('href'))