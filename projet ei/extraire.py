import requests
from bs4 import BeautifulSoup
import sys

url=f'http://127.0.0.1:{str(sys.argv[2])}/vidal/'
links=[]
rep=requests.get(url)
substances=[]
fiche=open('subst.dic','w',encoding='utf-16 LE')
fiche2=open('infos1.txt','w',encoding='utf-8')
fiche.write('\ufeff')
fiche2.write('\ufeff')
c=0
s=0
interval=sys.argv[1]
lettres='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

x=interval.split('-')
print(x)
deb=lettres.index(x[0])
fin=lettres.index(x[1])
for i in range(deb,fin+1):
    links.append(f'http://127.0.0.1:{str(sys.argv[2])}/vidal/vidal-Sommaires-Substances-{lettres[i]}.html')
print(links)

for link in links:
    url=link
    reponse=requests.get(url)
    if reponse.ok:
        soup=BeautifulSoup(reponse.text,'html.parser')
        uliste=soup.findAll('ul',{'class':'substances list_index has_children'})
        for ul in uliste:
            liste=ul.findAll('li')
            for li in liste:
                a=li.findAll('a')
                for i in a :
                    v=i.text
                    v=v.replace('Ã©','é')
                    v=v.replace('Ã¨','è')
                    v=v.replace('Ã¯','ï')
                    v=v.replace("Ãª",'ê')
                    fiche.write(v+',.N+subst'+'\n')
                    c+=1
        fiche2.write(f'pour {lettres[deb]}:'+str(c)+'\n')
        deb+=1
        s+=c
        c=0


fiche2.write(f'la somme:'+str(s)+'\n')
fiche2.close()
fiche.close()