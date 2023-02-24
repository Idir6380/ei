import sqlite3
from bs4 import BeautifulSoup
f = open('.\\corpus-medical_snt\\concord.html','r',encoding='utf-8').read()
soup = BeautifulSoup(f,'html.parser')
a = soup.findAll('a')
tab=[]
for i in a:
    v = i.text
    tab.append(v)
print(len(tab))
conct = sqlite3.connect('extraction.db')
cur = conct.cursor()
cur.execute("DROP TABLE IF EXISTS extraction")
cur.execute("CREATE TABLE extraction(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Posologie TEXT)")


cur.executemany("INSERT INTO extraction(Posologie) VALUES(?)", [(x,) for x in tab])
cur.execute('select * from extraction')
print(cur.fetchall())

conct.commit()
cur.close()
conct.close()