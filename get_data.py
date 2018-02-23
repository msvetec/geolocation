# -*- coding: utf-8 -*-
import requests
import json
import io
import webbrowser
import os
from urllib.request import pathname2url




jsonFile = []

def GetData(_townName):
    provjera = 1
    provjera2 = 0
    kriviUnos=0
    data = requests.get('http://dbpedia.org/data/'+_townName+'.json').json()
    if not data:
        print ("Grad ne postoji u bazi!!!!")
        
        
    else:
            town = data['http://dbpedia.org/resource/'+_townName]
            
            while True:
                try:
                    cityArea = town['http://dbpedia.org/ontology/areaTotal'][0]['value']
                    provjera = 0
                    break
                except:
                    break
            if provjera:
                while True:
                    try:
                        cityArea = town['http://dbpedia.org/ontology/areaUrban'][0]['value']
                        break
                    except:
                        provjera2=1
                        break
            if provjera2:
                while True:
                    try:
                        cityArea = town['http://dbpedia.org/ontology/area'][0]['value']
                        break
                    except:
                        print("Baza ne sadrzi podatke o povrsini grada!")
                        cityArea=0
                        break   
            while True:
                try:
                    population = town['http://dbpedia.org/ontology/populationUrban'][0]['value']
                    break
                except:
                    population = town['http://dbpedia.org/ontology/populationTotal'][0]['value']
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
            
    

def MakeJSON(_cityArea,_population,_elevation):
   jsonDict = {
       'Ime':townName,
       'Velicina':_cityArea/1000000,
       'Broj_stanovika':_population,
       'Nadmorska_visina':_elevation }
   jsonFile.append(jsonDict)
   return 

def WriteJSONFile(jsonFile):
    with io.open('dataJSON.json','w',encoding='utf-8') as f:
        f.write(json.dumps(jsonFile, sort_keys = False, ensure_ascii=False))
        f.close()
    return
    
def OpenHTML():
    url = 'file:{}'.format(pathname2url(os.path.abspath('index.html')))
    webbrowser.open(url,new=0)
    return


ans = 1
brojac = 0
while ans:
    print("=====================")
    print("1. Usporedba gradova")
    print("9. Kraj!")
    print("=====================")
    unos = int(input("Vas odabir: "))
    if unos == 1:
        jsonFile.clear()
        while True:
            try:
                brGradova=int(input("Koliko gradova zelite usporediti: "))
                while brojac!=brGradova:
                    townName = input("Unesite ime grada: ").title()
                    cityArea,population,elevation=GetData(townName)
                    MakeJSON(cityArea,population,elevation)
                    brojac=brojac+1
                WriteJSONFile(jsonFile)
                OpenHTML()
                break
            except:
                print("Krivi unos!")
                break
    elif unos==9:
        ans=0
        
        
    
    
    
