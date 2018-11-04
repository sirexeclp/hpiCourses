#%% imports
import requests
from lxml import html, etree
import pandas as pd
from urllib.parse import urljoin
import numpy as np
import pickle
import re

#%%
def get(url):
	"""Uses HTTP-GET to request a webresource and converts the result into html-object."""
	result = sessionRequests.get(url
		,headers=dict(referer = url))
	return html.fromstring(result.content)

def apply(self, other)->list:
	return list(map(other, self))

#%%
sessionRequests = requests.session()

baseURL = "https://hpi.de/studium/lehrveranstaltungen"

def getLVOverwievs(url) -> dict:
	"""crawls the main hpi courses website to obtain a list of courselists (eg. Bachelor, Master courses, etc.) """
	lvSuperList = get(url)
	lvOverviews = lvSuperList.xpath("//h1[contains(text(),'Lehrveranstaltungen')]//following-sibling::ul//a")
	return {x.text:x.get("href") for x in lvOverviews}

lvOverviews = getLVOverwievs(baseURL)

#expand to full path
lvOverviews = list(map(lambda x:urljoin(baseURL,x),lvOverviews.values()))


def extractDictOfCourses(url):
	"""Crawls a table-page with courses and returns a dict coursename and URL to coursepage """
	courseListPage = get(url)
	return {item.text.strip(): urljoin(url,item.get("href")) for item in
		 courseListPage.xpath("//div[@id = 'content']//table//tr//td[1]//a")}

#list of Courses
listOfCourses = list (map(extractDictOfCourses,lvOverviews))


def combineLinkList(linkList):
	"""combines the list of dicts to one big list, which only contains URLs"""
	return [courseLink for subject in 
		linkList for courseLink in subject.values()]

urlsToCrawl = combineLinkList(listOfCourses)

#%%
import time
def downloadCourseSites(urls,delay = 0.1):
	"""downloads the individual course websites """
	result = []
	for item in urls:
		result.append(get(item))
		print(f"got {item.split('/')[-1]}")
		time.sleep(delay)
	return result

courseWebsites = downloadCourseSites (urlsToCrawl)


#%% save/load crawled websites with pickle

# courseWebsitesString = [etree.tostring(x) for x in courseWebsites]

# with open("websites.pkl","wb") as file:
# 	pickle.dump(courseWebsitesString, file)
#%%
"""uncomment this to load the locally saved websites"""
# with open("websites.pkl","rb") as file:
# 	cws = pickle.load(file)

# courseWebsites = [html.fromstring(x) for x in cws]

#%%
def findAllFiles(secondPage, secondURL, fileExtension):
	"""Finds all Links, on given website at given url that destination ends with
	the given fileextension."""
	assert secondPage, "Second page must not be 'None'."
	return [urljoin(secondURL,x) for x in 
		secondPage.xpath(f"//a[contains(@href,'{fileExtension}')]/@href")]

#%%
"""lets create a list of dicts where each dict holds infos about one course"""
allCourses = []
for site,url in zip(courseWebsites, urlsToCrawl):
	course = {}
	#get the main heading of the coursesite which should contain the coursename and semester
	fullTitle = site.xpath("//h1[1]/text()")[0]
	#use this regex to split coursename and semester
	matches = re.search(r"(.*)\((.*)\)",fullTitle)

	if matches:
		course["Name"] = matches[1]
		course["Semester"] = matches[2]
	else:
		#if regex did not match anything, just use the whole headline as coursetitle and 
		#assume theres no semester given
		course["Name"] = fullTitle
	course["URL"] = url
	#find the link after '...Website', which should be the link to the 2nd course page
	secondURL = site.xpath("//div/text()[contains(.,'Website')]/following-sibling::i/a/@href")
	secondURL = secondURL[0] if secondURL else None
	secondPage = None
	if secondURL:
		course["secondURL"] = secondURL
		secondPage = get(urljoin(url,secondURL))
		course["files"] = findAllFiles(secondPage, secondURL, ".pdf")
	
	#extract all basic infos from a list on the course page
	for item in site.xpath("//h2[contains(text(),'Allgemeine Information')]/following-sibling::ul[1]//li//text()"):
		if len(item.split(":")) == 2:
			key,val = item.split(":")
			course[key] = val.strip()
	allCourses.append(course)




#%%
"""Create a DataFrame from the dicts"""
df = pd.DataFrame(columns=["Name"
	,"Website"
	,"Belegungsart"
	,"Benotet"
	,"ECTS"
	,"Einschreibefrist"
	,"Lehrform"
	,"Lehrsprache"
	,"Semesterwochenstunden"
	,"URL"
	,"files"
	,"secondURL"
	])
df = df.append(allCourses,ignore_index = True)

#remove duplicates, but ignore files and URL column
duplicatesRemoved = df.drop_duplicates(df.columns.difference(["files","URL"]))

