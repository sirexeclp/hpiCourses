#%%


pdfFile = r"C:\Users\ktvsp\Downloads\Verlegungsplan_KW_46_.pdf"

import PyPDF2
import re

text = PyPDF2.PdfFileReader(open(pdfFile,"rb"))

text =text.getPage(0).extractText().split("\n")

date = None
meineLvs = ["Data Preperation for Science","Cloud","Algo","HCI","Distributed"]#, "Network Security in Practice", "Visualization",  "Business Process Analysis in Healthcare"]
it = iter(filter(None,text))
items = []
for line in it :
	if isDate(line):
		#from dateutil.parser import parse
		date = (line.split(",")[1])
	elif date:
		item = {}
		item["date"] = date.strip()
		item["courseName"], item["teacher"] = [x.strip() for x in line.split(" - ")]
		line = next(it)
		item["time"] = extractTime(line).strip()
		item["room"] = extractRoom(line).strip()	
		items.append(item)
items
[x for x in items for y in meineLvs  if y in x["courseName"]  ]
	#if any(filter(lambda x: x in line,meineLvs)):
	#	print(f"{date} {extractRoom(text[index+1])}-- {line} -- {extractTime(text[index+1])}")

def isDate(text):
	days = ["Montag","Dienstag","Mittwoch","Donnerstag"
			,"Freitag","Samstag","Sonntag"]
	return any([x in text for x in days])

def extractTime(text):
	
	tmp = re.search("(\d\d.*\d\d) Uhr",text)
	if tmp:
		return tmp[1]
	else:
		return ""
def extractRoom(text):
	tmp = re.search("verlegt in (.*)",text)
	if tmp:
		return tmp[1]
	else:
		return text.split("-")[-1]
from tabula import read_pdf
import tabula
testdf = read_pdf(
	#pdfFile
	r"C:\Users\ktvsp\OneDrive\Orgel\Liedplan\2018\8 Liedplan Sonntage 14.10.2018 - 04.11.2018.pdf"
	, java_options="-Dfile.encoding=UTF8")
testdf = testdf.T

testdf.dropna(axis='columns',how = "all")

testdf[testdf[0]=="4. November"]

import django