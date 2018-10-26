import requests
from lxml import html
import pandas as pd


def get(url):
    result = sessionRequests.get(url
		,headers=dict(referer = url))
    return html.fromstring(result.content)

sessionRequests = requests.session()

lvItSe = get("https://hpi.de/studium/lehrveranstaltungen/it-systems-engineering-ma.html")

listOfCourses = lvItSe.xpath("//div[@id = 'c6584']//tr//td[1]//a/@href")

results = []
for courseLink in listOfCourses:
    courseWebsite = get("https://hpi.de/"+courseLink)
    tmp = courseWebsite.xpath("//h1[1]/text()")
    tmp.extend(courseWebsite.xpath("//div[@id = 'c6681']//ul[1]//li//text()"))
    results.append(tmp)

dicts = []
for line in results:
    tmp = {}
    tmp["Name"] = line[0]
    for item in line:
        if len(item.split(":")) == 2:
            key,val = item.split(":")
            tmp[key] = val.strip()
    dicts.append(tmp)


df = pd.DataFrame(columns=["Name","Belegungsart","Benotet","ECTS","Einschreibefrist","Lehrform","Lehrsprache","Semesterwochenstunden"])
df = df.append(dicts,ignore_index = True)
df