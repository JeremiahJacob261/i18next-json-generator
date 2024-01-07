import requests
import json
import ast
import codecs
from bs4 import BeautifulSoup
import os
from pathlib import Path
#packages to install : bst:beautifulsoup,
#packages used : requests, os, json,bs4

paths = str(Path.cwd());
list = ['en', 'es', 'vi', 'ru', 'fr', 'pl','de']
#the list of langu

mlist = ''
for m in list:
    rmlist = list[list.index(m)]
    if( list.index(m) > 0):
        mlist = mlist + ',' + rmlist
    else:
        mlist = mlist + rmlist


#must read
#the above is to be edited' var list , a list of a the list of country language code is to filled in the array
#remember you are using my api key, please responsibly. or add yours
#get your at https://microsoft-translator-text.p.rapidapi.com/translate

def run(url,name):
    print('Generating...'+name)

    #the below connects to the rapid API server
    def getTran(text):
        url = "https://microsoft-translator-text.p.rapidapi.com/translate"

        querystring = {"to[0]": mlist, "api-version": "3.0", "profanityAction": "NoAction",
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
        trtext = {}
        #remember this is a custom code

        for tx in list:
            trtext[tx] = translation[list.index(tx)]['text']

        #the is the end of my custom code
        # print(trtext)
        return trtext

    #the below scraps the data from your website
    def get_text(url, filee):
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
                    translated_txt = codecs.decode(getTran(p.text)[l], 'unicode_escape')
                    extract = extract | {p.text.replace(" ", ""): translated_txt}
                    # print(getTran(p.text)[l])

            path = paths +  r'/'  + l
            # Create the directory
            os.makedirs(path, exist_ok=True)
            filename = filee+'.json'
            with open(os.path.join(path, filename), 'w') as fp:
                json.dump(extract, fp)

    # Use the function
    return get_text(url,name)
#list of url and nname of file you want store the data as
#key url as the url of the page
#key name as the url of the page
#examples : pages = [{'url':'https://www.sfcsports01.com/dashboard/codesetting','name':'codesetting'},{'url':'https://www.sfcsports01.com/dashboard/transactions','name':'transactions'}]
# pages = [{'url':'https://www.wikipedia.com','name':'wiki'}]
# for p in pages:
pd = True
px = input("input the website's url : ")
pn = input("what name do you wish to name the data file ? : ")

def vo():
    run(px,pn)
    pr = input("do you want to generate data for another page ? yes/no (y/n) : ")
    if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
        vo();
    else:
        print("Thanks for Using my tool, please give a STAR on GITHUB")
vo()



#this is the end of the code, more updates will appear soonest.