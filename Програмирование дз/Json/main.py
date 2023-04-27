import json

with open('datafile.json', 'r') as my_file:
    name_person = json.loads('name')
    planet_person = json.loads('planet')
    series_person = json.loads('episode')
print(name_person, planet_person, series_person)


