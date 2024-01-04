import requests
import json
import ast
from bs4 import BeautifulSoup
import os

#packages to install : bst:beautifulsoup,
#packages used : requests, os, json,bs4

paths = input('input the location you wish to atore the data, eg, C:\\Users\\user\Documents\python_project/')

list = ['en', 'es', 'vi', 'ru', 'fr', 'pl']
#must read
#the above is to be edited' var list , a list of a the list of country language code is to filled in the array
#remember you are using my api key, please responsibly. or add yours
#get your at https://microsoft-translator-text.p.rapidapi.com/translate

def run(url,name):
    print('Generating...'+name)

    #the below connects to the rapid API server
    def getTran(text):
        url = "https://microsoft-translator-text.p.rapidapi.com/translate"

        querystring = {"to[0]": "es,vi,ru,fr,pl", "api-version": "3.0", "profanityAction": "NoAction",
                       "textType": "plain"}

        payload = [{"Text": text}]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "7939998216msh540c9956d3a0d42p1113fbjsn088965af1f71",
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers, params=querystring)
        results = response.json()
        translation = results[0]['translations']

        #remember this is a custom code
        estext = translation[0]['text']
        vitext = translation[1]['text']
        rutext = translation[2]['text']
        frtext = translation[3]['text']
        pltext = translation[4]['text']
        trtext = {'es':estext,'vi':vitext,'ru':rutext,'fr':frtext,'pl':pltext}
        #the is the end of my custom code

        return trtext

    #the below scraps the data from your website
    def get_scores(url, filee):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')
        extract = {}
        # Write the data dictionary to a JSON file

        for l in list:
            if l == 'en':
                # the scrapper only scraps to data that are in the <p> tags
                # the key is same as the value of the website defaults language with no spaces
                for p in soup.find_all('p'):
                    extract = extract | {p.text.replace(" ", ""): p.text}
            else:
                for p in soup.find_all('p'):
                    extract = extract | {p.text.replace(" ", ""): getTran(p.text)[l]}
                    # print(getTran(p.text)[l])

            path = paths  + l
            # Create the directory
            os.makedirs(path, exist_ok=True)
            filename = filee+'.json'
            with open(os.path.join(path, filename), 'w') as fp:
                json.dump(extract, fp)

    # Use the function
    return get_scores(url,name)
#list of url and nname of file you want store the data as
#key url as the url of the page
#key name as the url of the page
#examples : path = [{'url':'https://www.sfcsports01.com/dashboard/codesetting','name':'codesetting'},{'url':'https://www.sfcsports01.com/dashboard/transactions','name':'transactions'}]
pages = []
for p in pages:
    run(p['url'],p['name'])
#this is the end of the code, more updates will appear soonest.