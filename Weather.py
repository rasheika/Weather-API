import requests
from bs4 import BeautifulSoup
''' strip and split text[:60]'''

def kingston():
	URL = requests.get("https://www.accuweather.com/en/jm/kingston/214971/weather-forecast/214971")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def standrew():
	URL = requests.get("https://www.accuweather.com/en/jm/half-way-tree/409011/weather-forecast/409011")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def stthomas():
	URL = requests.get("https://www.accuweather.com/en/jm/morant-bay/215037/weather-forecast/215037")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def portland():
	URL = requests.get("https://www.accuweather.com/en/jm/port-antonio/214755/weather-forecast/214755")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def stann():
	URL = requests.get("https://www.accuweather.com/en/jm/saint-anns-bay/214974/weather-forecast/214974")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def stmary():
	URL = requests.get("https://www.accuweather.com/en/jm/port-maria/215028/weather-forecast/215028")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)
	
def trelawny():
	URL = requests.get("https://www.accuweather.com/en/jm/falmouth/216200/weather-forecast/216200")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)
	
def stjames():
	URL = requests.get("https://www.accuweather.com/en/jm/montego-bay/215019/weather-forecast/215019")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def hanover():
	URL = requests.get("https://www.accuweather.com/en/jm/lucea/213182/weather-forecast/213182")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)
	
def westmoreland():
	URL = requests.get("https://www.accuweather.com/en/jm/savanna-la-mar/216714/weather-forecast/216714")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def stelizabeth():
	URL = requests.get("https://www.accuweather.com/en/jm/braes-river/220400/weather-forecast/220400")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def manchester():
	URL = requests.get("https://www.accuweather.com/en/jm/mandeville/214050/weather-forecast/214050")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def clarendon():
	URL = requests.get("https://www.accuweather.com/en/jm/may-pen/212602/weather-forecast/212602")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def stcatherine():
	URL = requests.get("https://www.accuweather.com/en/jm/spanish-town/214999/weather-forecast/214999")
	HTML = BeautifulSoup(URL.content,"html.parser")
	Cond = HTML.find_all("li",{"class":"day current first cl"})
	for x in range(len(Cond)):
		parish = (Cond[x])
		parish = parish.text[:60].replace("\n", " ").lstrip()
		temperature = parish[16:25].lstrip() 
		condition = parish[40:]
		print("\nCurrent Weather\n"+temperature+"\n"+condition)

def process_default():
	print("Error")

parishes = ["Kingston", "St. Andrew", "St. Thomas", "Portland", "St. Ann", "St. Mary", 
"Trelawny", "St. James", "Hanover", "Westmoreland", "St. Elizabeth","Manchester", "Clarendon", "St. Catherine"]

print("CURRENT WEATHER SYSTEM:\n")

for x in range(0,14):
	print(str(x+1)+".\t", parishes[x])

try:
	num=int(input("\nEnter a parish code(1-14) to view the current weather:\t"))
	options = {
	1: kingston,
	2: standrew,
	3: stthomas,
	4: portland,
	5: stann,
	6: stmary,
	7: trelawny,
	8: stjames,
	9: hanover,
	10: westmoreland,
	11: stelizabeth,
	12: manchester,
	13: clarendon,
	14: stcatherine,
	}
	options[num]()
except:
	print("Invalid Key!")