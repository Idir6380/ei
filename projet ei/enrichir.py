import sys
import re
tab=[]
extrait=[]
lettres='abcdeéfghijklmnopqrstuvwxyz'
f1=open(sys.argv[1],'r',encoding='UTF-8')

x=f1.readlines()

for i in x:
    reg = re.search(r'''
    ^[-*Ø]?\s?  # Debut avec "* " ou "- "
    (\w+)       #La substance recherchée 
    \s:?\s?     #subts :  (GAVISCON : 1 sachet par jour.)
    (\d+|,|\d+.\d)+
    \s?:?   
    (\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)
    ''', i, re.VERBOSE | re.I)    
    if reg :
            if  reg.group(1).lower() != 'vichy' \
                and reg.group(1).lower() != 'mdz' \
                and reg.group(1).lower() != 'vvp' \
                and reg.group(1).lower() != 'hémoglobine' \
                and reg.group(1).lower() != 'aspegic'  \
                and reg.group(1).lower() != 'kt' \
                and reg.group(1).lower() != 'le' \
                and reg.group(1).lower() != 'puis':
                extrait.append(reg.group(1).lower()+',.N+subst'+'\n')
f1.close()
print(len(extrait))
#creation subst_corpus.dic
p=open('subst_corpus.dic','w',encoding='UTF-16 LE') 
p.write('\ufeff')  
for i in extrait:
    p.write(i)
extrait = sorted(list(set(extrait)))

#MAJ subst.dic
print(len(extrait))
f2=open('res.txt','w',encoding='UTF-8')
for i in extrait:
    f2.write(i)
f2.close()

f2=open('res.txt','r',encoding='UTF-8')
f=open('subst.dic','r',encoding='utf-16')

#creation info3.txt
inf3=open('infos3.txt','w',encoding='UTF-8')
resultat=f2.readlines()
resgle=f.readlines()

resultat=sorted(list(set(resultat)))
resgle=sorted(list(set(resgle)))
s=0
for let in lettres:
    c=0
    for r in resultat:
        if r[0]==let:
            if r not in resgle:
                inf3.write(r)
                c+=1
    inf3.write('-'*100+'\n')
    inf3.write(f'pour {let}:{str(c)}\n')
    inf3.write('-'*100+'\n')
    s+=c
    c=0
    
inf3.write(f'resultat a ajouter:{s}')


s=0
c=0
#creation info2.txt
f2=open('res.txt','r',encoding='UTF-8')
f3=open('infos2.txt','w',encoding='UTF-8')
for lettre in lettres:
    for ext in extrait:
        
        if ext[0]==lettre:
            f3.write(ext)
            c+=1
    f3.write('-'*100+'\n')
    f3.write(f'total de {lettre}:{str(c)} \n')
    f3.write('-'*100+'\n')
    s+=c
    c=0
f3.write(f'Nombre de medicaments issus de corpus de corpus medical:{s} \n') 
f3.close()  
f2.close()

f2=open('res.txt','r',encoding='UTF-8')                
res=f2.readlines()
for e in res:
    if e not in tab:
        tab.append(e)
f2.close()
f2=open('res.txt','w',encoding='UTF-8')
for e in tab:
    f2.write(e)
f2.close()
f2=open('res.txt','r',encoding='UTF-8')                
res=f2.readlines()
f2.close()
f3=open('subst.dic','r',encoding='utf-16')
x=f3.readlines()
for i in x:
    if i not in res:
        res.append(i)
res = sorted(list(set(res)))
f3.close()
#mise a jour final subst.dic
f3=open('subst.dic','w',encoding='utf-16')
f3.write('\ufeff')
for e in res:
    f3.write(e)
f3.close()

