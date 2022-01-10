import os
basedir = input("Entrer le chemin d'accès des dossiers à raccourcir : ")

for fn in os.listdir(basedir):
    print(fn)