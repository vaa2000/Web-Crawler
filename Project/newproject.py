import requests
from bs4 import BeautifulSoup


print("Options to search for unversities are as follows")
print("Enter option 1 for Well-Known Unversities in Asia-Pacific region")
print("Enter option 2 for Universities in North America(most of them from USA)")
print("Enter option 3 for Universities in South America")
print("Enter option 4 for Universities in Europe")
print("Enter option 5 for Universities in Australia")



print('Enter option according to region in which you want to study')
country=int(input())
print(f'Filtering out {country}')

if country == 1:    
    url="https://www.timeshighereducation.com/student/best-universities/best-universities-asia-pacific-region"
    r=requests.get(url)
    htmlContent = r.content
    
    soup=BeautifulSoup(htmlContent,'html.parser')

    elements=soup.select("td > a")
    item=[]
    for i in elements:
        if i is not None:
            item.append(i)
    print(item)


