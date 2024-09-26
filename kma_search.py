#Importer les librairies os et glob

import os
import glob2

#Definir le repertoire de travail, ici le repertoire de travail est la ou se trouve le script
pwd=os.system("pwd")
os.chdir=pwd

#
R1=glob2.glob("*_1.*gz")
R2=glob2.glob("*_2.*gz")

#Ranger les reads par ordre alphabetique pour qu'ils soient traites 2 à 2
R1.sort()
R2.sort()

# Vérifier que les reads ont bien été classés par ordre alphabétique
print(R1)
print(R2)

# Lancer l'algorithme KMA avec l'option paire-reads en renseignant le read forward et reserve 
# Le gène recherché (repL) doit aussi être renseigné après avoir été indexé dans une base de donnée de type KMA
# Ici le gène repL est dans /home/sadio/
for i in range(len(R1)):
        os.system(" kma -ipe "+R1[i]+" "+R2[i]+" -o repL_"+R1[i]+" -t_db /home/sadio/repL_kma")   
