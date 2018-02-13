# -*- coding: utf-8 -*-
import requests
import json
import io



jsonFile = {}

def GetData(_townName):
    
    data = requests.get('http://dbpedia.org/data/'+_townName+'.json').json()
    town = data['http://dbpedia.org/resource/'+_townName]
    cityArea = town['http://dbpedia.org/ontology/areaTotal'][0]['value']
    population = town['http://dbpedia.org/ontology/populationTotal'][0]['value']
    elevation = town['http://dbpedia.org/ontology/elevation'][0]['value']

    return cityArea,population,elevation
    

    

def MakeJSON(_cityArea,_population,_elevation):
   
    jsonFile[townName] = {
        'Velicina':_cityArea,
        'Broj stanovika':_population,
        'Nadmorska visina':_elevation }
    return 

def WriteJSONFile(jsonFile):
    with io.open('test.json','w',encoding='utf-8') as f:
        f.write(json.dumps(jsonFile, sort_keys = True, ensure_ascii=False))
    

unos = int(input("Unesite broj gradova: "))
for i in range(0,unos):
    
    townName = input("Unesite ime grada: ")
    cityArea,population,elevation=GetData(townName)
    MakeJSON(cityArea,population,elevation)

    

WriteJSONFile(jsonFile)
