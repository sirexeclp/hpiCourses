#%%


pdfFile = r"C:\Users\ktvsp\OneDrive\Studium\HPI\Verlegungsplan_KW_45.pdf"

import PyPDF2

text = PyPDF2.PdfFileReader(open(pdfFile,"rb"))

text =text.getPage(0).extractText().split("\n")

date = str()
meineLvs = ["Algorithmix"]#, "Network Security in Practice", "Visualization",  "Business Process Analysis in Healthcare"]
for index,line in enumerate(text):
	if isDate(line):
		from dateutil.parser import parse
		date = parse(line.split(",")[1])
	if any(filter(lambda x: x in line,meineLvs)):
		print(f"{date} -- {line} -- {extractTime(text[index+1])}")

def isDate(text):
	days = ["Montag","Dienstag","Mittwoch","Donnerstag"
			,"Freitag","Samstag","Sonntag"]
	return any([x in text for x in days])

def extractTime(text):
	return re.search("(\d\d.*\d\d) Uhr",text)[1]

from tabula import read_pdf
import tabula
testdf = read_pdf(
	#pdfFile
	r"C:\Users\ktvsp\OneDrive\Orgel\Liedplan\2018\8 Liedplan Sonntage 14.10.2018 - 04.11.2018.pdf"
	, java_options="-Dfile.encoding=UTF8")
testdf = testdf.T

testdf.dropna(axis='columns',how = "all")

testdf[testdf[0]=="4. November"]