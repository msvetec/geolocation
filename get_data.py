# -*- coding: utf-8 -*-
import requests
import json
import io
import webbrowser
import os
from urllib.request import pathname2url




jsonFile = []

#dohvacanje podataka iz baze znanja DBpedia i vracanje informacija o gradu/drzavi/zupaniji koje se spremaju u jsonDict rijecnik
def GetData(_townName):
<<<<<<< HEAD
    provjera = 1
    provjera2 = 0
    
    data = requests.get('http://dbpedia.org/data/'+_townName+'.json').json()
    if not data:
        print ("Grad ne postoji u bazi!!!!")
        kriviUnos=1
        cityArea=0
        population=0
        elevation=0
        return cityArea,population,elevation        
    else:
            town = data['http://dbpedia.org/resource/'+_townName]
            kriviUnos=0
=======
   
    data = requests.get('http://dbpedia.org/data/'+_townName+'.json').json()
    while True:
        try:
            town = data['http://dbpedia.org/resource/'+_townName]
            
            
>>>>>>> parent of 7cdcb74... beta2
            while True:
                try:
                    cityArea = town['http://dbpedia.org/ontology/area'][0]['value']
                    break
                except:
                    cityArea = town['http://dbpedia.org/ontology/areaTotal'][0]['value']
                    break
                else:
                    cityArea = town['http://dbpedia.org/ontology/areaUrban'][0]['value']
                    break
                    
            while True:
                try:
                    population = town['http://dbpedia.org/ontology/populationTotal'][0]['value']
                    break
                except:
                    population = town['http://dbpedia.org/ontology/populationUrban'][0]['value']
                    break
            while True:
                try:
                    elevation = town['http://dbpedia.org/ontology/elevation'][0]['value']
                    break
                except:
                    print("Nadmorska visina grada nije definirana")
                    elevation = 0
                    break
            return cityArea,population,elevation
        except:
            print("Grad ne postoji")
            break
    
#Kreiranje .json datoteke na temelju jsonDict rijecnika
def MakeJSON(_cityArea,_population,_elevation):
<<<<<<< HEAD
   jsonDict = {
       'Ime':townName,
       'Velicina':_cityArea/1000000,
       'Broj_stanovika':_population,
       'Nadmorska_visina':_elevation }
   jsonFile.append(jsonDict)
   return 
#kreiranje .json da datoteke u direktoriju programa koja se ucitava u index.html 
=======
   for i in range (0,unos):
       jsonDict = {
           'Ime':townName,
           'Velicina':_cityArea/1000000,
           'Broj_stanovika':_population,
           'Nadmorska_visina':_elevation }
       jsonFile.append(jsonDict)
       return 

>>>>>>> parent of 7cdcb74... beta2
def WriteJSONFile(jsonFile):
    with io.open('dataJSON.json','w',encoding='utf-8') as f:
        f.write(json.dumps(jsonFile, sort_keys = False, ensure_ascii=False))
        f.close()
    return
#otvaranje index.html datoteke u defoltnom web pregledniku.   
def OpenHTML():
    url = 'file:{}'.format(pathname2url(os.path.abspath('index.html')))
    webbrowser.open(url,new=0)
    return


ans = 1
<<<<<<< HEAD
brojac = 0
kriviUnos=1
=======
>>>>>>> parent of 7cdcb74... beta2
while ans:
    print("=====================")
    print("1. Usporedba gradova")
    print("9. Kraj!")
    print("=====================")
    unos = int(input("Vas odabir: "))
    if unos == 1:
        jsonFile.clear()
<<<<<<< HEAD
       # while True:
           # try:
        brGradova=int(input("Koliko gradova zelite usporediti: "))
        while brojac!=brGradova:
            
            
            townName = input("Unesite ime grada: ").title()
            cityArea,population,elevation=GetData(townName)
            if kriviUnos==1:
                print("Krivi unos podataka")
            else:
                kriviUnos=0
                MakeJSON(cityArea,population,elevation)
                brojac=brojac+1
           
        WriteJSONFile(jsonFile)
        OpenHTML()
                #break
            #except:
               # print("Krivi unos!")
                #break
=======
        while True:
            try:
                brGradova=int(input("Koliko gradova zelite usporediti: "))
                for i in range(0,brGradova):
                    townName = input("Unesite ime grada: ").title()
                    cityArea,population,elevation=GetData(townName)
                    MakeJSON(cityArea,population,elevation)
                WriteJSONFile(jsonFile)
                OpenHTML()
                break
            except:
                print("Krivi unos!")
                break
>>>>>>> parent of 7cdcb74... beta2
    elif unos==9:
        ans=0
        
        
    
    
    
