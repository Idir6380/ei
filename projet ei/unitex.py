import os
from os import path
if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt Dela_fr.bin subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
#le fichier alphabet.txt est pris à la tokenisation il sert a preciser la langue à prendre en consideration donc on le prend dans la premiére phase du script
# le sens où la liste token ne sera pas chargé
#donc il reconnaitra  pas mal de mot et carctére qui se trouve dans le graph posologie
#exemple en efacant la ligne Bb du fichier Alphabet.txt on remarque que nombre de match à été reduit à 1198 match or tout les mots que reconnait le
#graph mais comportant la lettre b ne sont plus reconnu exmple de la substance :tazobactam pour cet exemple là.
#or de ce qu'on a compris le graph est un outil pour trouver nos match mais l'alphbet.txt sert à les verifié et reconnaitre et on aura les resultats
#reconnu grace à alphabet en bleu dans concorde en d'autre terme c'est grace a cette alphabet que le graph reconnait ses match
#c'est comme une sorte de grammaire lexical