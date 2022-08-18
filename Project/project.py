#   NAME : VAISHNAVI A. AINAPURE
#   EMAIL-ID: 2018.vaishnavi.ainapure@ves.ac.in
#   Contact No:  +91 9619843114 
#   College: Vivekanand Education Society’s Institute of Technology, Chembur

import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.computersciencedegreehub.com/50-innovative-computer-science-departments/"

#1
r = requests.get(url)
htmlContent = r.content

#2
soup=BeautifulSoup(htmlContent,'html.parser')

#3

#nd = soup.find(class='entry-content')
#for elem in nd.contents:
item = soup.select("h3 > a")
item1 = soup.select(".entry-content > h3")

url1 = []
dict1={}
for i in item:
    url1.append(i.get('href'))

#print(url1)


#with open("file.csv", "w") as f:
#    f.write("UNIVERSITY NAME: ,UNIVERSITY CONTACT DETAILS AND EMAIL(acc to given details):,NAME OF DEPARTMENT:\n")
    

k=1
z=1
m=0
while m<len(url1):
    if url1[k] is not None:
        r1=requests.get(url1[k])
        htmlContent = r1.content
        soup1=BeautifulSoup(htmlContent , 'html.parser')
        
        if soup1 is not None:
            print(z," ")
            if soup1.h1 is not None:
                print("UNIVERSITY NAME: ", item1[m].get_text())
                print("\n")
            if soup1.footer is not None:   
                print("UNIVERSITY CONTACT DETAILS AND EMAIL(acc to given details):",soup1.footer.get_text())
            print("NAME OF DEPARTMENT:",item[k].string)
            print("\n")
           # f.write(item1[m].get_text(),soup1.footer.get_text(),item[k].string)
            k=k+2 
            z=z+1
            m=m+1
            print("---------------------------------------------------------------------------------------------")
            if item1[m] is None or soup1.footer is None or item[k] is None:
                dict1[m]=["None","None","None"]
            else:
                dict1[m]=[item1[m].get_text(),soup1.footer.get_text(),item[k].string]
        else:
            pass    
    else:
        pass    


dict1_df=pd.DataFrame.from_dict(dict1,orient = 'index' ,columns = ["UNIVERSITY NAME: ","UNIVERSITY CONTACT DETAILS AND EMAIL(acc to given details):]","NAME OF DEPARTMENT:"])
#dict1_df.head()
dict1_df.to_csv('dict1.csv')
