import requests
from bs4 import BeautifulSoup

url="https://studyabroad.shiksha.com/be-btech-in-computer-science-engineering-from-abroad-ds11510277"

#1
r = requests.get(url)
htmlContent = r.content

#2
soup=BeautifulSoup(htmlContent,'html.parser')
item=soup.find_all("div",class_="tuple-image")


url1=[]
for i in item:
    url1.append(i.a.get('href'))

k=0
z=1
m=0
while k<len(url1):
    if url1[k] is not None:
        r1=requests.get(url1[k])
        htmlContent = r1.content
        soup1=BeautifulSoup(htmlContent , 'html.parser')
        
        if soup1 is not None:
        #    print(z," ")
            url2=[]
            elem = soup1.select("td > a")
            for j in elem:
                url2.append(j.get('href'))
    k=k+1    
    z=z+1
print()