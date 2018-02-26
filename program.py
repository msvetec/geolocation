# -*- coding: utf-8 -*-
import requests
import json
import io
import webbrowser
import os
from urllib.request import pathname2url



jsonCreated = 0
jsonFile = []
#dohvacanje podataka iz baze znanja DBpedia i vracanje informacija o gradu/drzavi/zupaniji koje se spremaju u jsonDict rijecnik
def GetData(_brPonavljanja):
    provjeraA1 = 0
    provjeraA2 = 0
    provjeraP1 = 0
    brojac = 0

    
    while brojac != _brPonavljanja:
        townName = input("Unesite ime grada: ").title()   
        data = requests.get('http://dbpedia.org/data/'+townName+'.json').json()
        if not data:
            print ("Unos ne postoji u DBpedia bazi!!!!")
             
        else:
            town = data['http://dbpedia.org/resource/'+townName]
            kriviUnos=0
            #dohvacanje podataka o povrsini
            #zbog nepotpunosti baze podataka prvo se pronaleze podaci o samom gradu a ako nisu navedene onda se uzme u obzir i urbani dio
            #nedostata baze znanja je i taj sto nisu isti pojmovi jednako definirani kao npr kod Parisa povrsina se nalazi pod upitom /area a ne kao kod ostalih gdje je taj podatak u /areaTotal
            while True:
                try:
                    cityArea = town['http://dbpedia.org/ontology/areaTotal'][0]['value']
                    break
                except:
                    provjeraA1 = 1
                    provjeraA2 = 0
                    break
            if provjeraA1:
                while True:
                    try:
                        cityArea = town['http://dbpedia.org/ontology/areaUrban'][0]['value']
                        provjeraA1=0
                        break
                    except:
                        provjeraA1 = 0
                        provjeraA2 = 1
                        break
            if provjeraA2:
                while True:
                    try:
                        cityArea = town['http://dbpedia.org/ontology/area'][0]['value']
                        provjeraA2 = 0
                        break
                    except:
                        print("Baza ne sadrzi podatke o povrsini!")
                        provjeraA2 = 0
                        cityArea = 0
                        break
            #dohvacanje podataka o populaciji
            while True:
                try:
                    population = town['http://dbpedia.org/ontology/populationTotal'][0]['value']
                    break
                except:
                    provjeraP1 =1
                    break
            if provjeraP1:
                while True:
                    try:
                        population = town['http://dbpedia.org/ontology/populationUrban'][0]['value']
                        provjeraP1 = 0
                        break
                    except:
                        population = 0
                        provjeraP1 = 0
                        print("Baza ne sadrži podatke o populaciji!")
                        break
            #dohvacanje podataka o nadmorskoj visini
            while True:
                try:
                    elevation = town['http://dbpedia.org/ontology/elevation'][0]['value']
                    break
                except:
                    elevation = 0
                    print("Nadmorska visina nije definirana")
                    break
            if cityArea==0 and population==0 and elevation==0:
               print("Ne radi se o gradu!!!")
            else:
                MakeJSON(cityArea,population,elevation,townName)
                brojac = brojac + 1
             
#Kreiranje .json datoteke na temelju jsonDict rijecnika
def MakeJSON(_cityArea,_population,_elevation,_townName):
    jsonCreated = 1
    for i in range (0,unos):
        jsonDict = {
            'Ime':_townName,
            'Velicina':_cityArea/1000000,
            'Broj_stanovika':_population,
            'Nadmorska_visina':_elevation }
        jsonFile.append(jsonDict)
    return 
#kreiranje .json da datoteke u direktoriju programa koja se ucitava u graphDraw.js
def WriteJSONFile(jsonFile):
    with io.open('dataJSON.json','w',encoding='utf-8') as f:
        f.write(json.dumps(jsonFile, sort_keys = False, ensure_ascii=False))
        f.close()
    return
#provjera postojanja .json datoteke i otvaranje index.html datoteke u defoltnom web pregledniku.       
def OpenHTML():
    fname="dataJSON.json"
    if os.path.isfile(fname):
        url = 'file:{}'.format(pathname2url(os.path.abspath('index.html')))
        webbrowser.open(url,new=0)
    else:
        print("Podaci ne postoje odaberite opciju 1.")
   

        
ans = 1
unosBroja = 0
while ans:
    print("=====================")
    print("1. Usporedba gradova")
    print("2. Otvori postojece analize")
    print("9. Kraj!")
    print("=====================")
    unos = int(input("Vas odabir: "))
    if unos == 1:
        jsonFile.clear()
        while True:
            try:
                brGradova = int(input("Koliko gradova zelite usporediti: "))
                unosBroja = 1
                break
            except:
                print("Krivi unos!!!")
                unosBroja = 0
                break
        if unosBroja:
            GetData(brGradova)
            WriteJSONFile(jsonFile)
            OpenHTML()
    elif unos==2:
        OpenHTML()
    elif unos==9:
        ans=0
        
        
    
    
    
