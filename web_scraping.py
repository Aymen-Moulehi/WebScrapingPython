import requests
from bs4 import BeautifulSoup
import random





res = requests.get("http://www.fss.rnu.tn/fra/s1269/departements/INC/6/")
src = res.content
soup = BeautifulSoup(src,"lxml")
profs_names = soup.find_all("div",{"class":"h2"})
names =[RecursionError]
for i in profs_names:
    names.append(i.text)

while(True):
    print("1- Get random name ")
    print("2- Exit")
    x = input(">>>")
    if(x == '1'):
        name = random.choice(names)
        print(name)
    elif(x == '2'):
        exit()
    else:
        print("!!!")





