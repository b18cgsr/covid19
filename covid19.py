
#from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
import time

#country = "USA"
country = input("Country to check: ") 
#city=input("What city to check: ") 
notification_duration = 10
refresh_time = 10 #minutes
data_check= []
worldmetersLink = "https://www.worldometers.info/coronavirus/"
#world_usa_city=(f"https://www.worldometers.info/coronavirus/country/{country.lower()}")
#print(world_usa_city)

def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+","")
        i = i.replace("-","")
        i = i.replace(",",",")#removed . 
        if i == "":
            i = "0"
        L.append(i.strip())
    return L

while True:
    try:
        html_page = requests.get(worldmetersLink)
    except requests.exceptions.RequestException as e: 
        print (e)
        continue
    bs = BeautifulSoup(html_page.content, 'html.parser')

    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) !=-1:
            start = i
            break
    data = []
    for i in range(1,8):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]
    
    data= data_cleanup(data)
    message = "\nTotal infected = {} \nNew Case = {} \nTotal Deaths = {} \nNew Deaths = {} \nRecovred = {} \nActive Case = {} \nSerious Critical = {}".format(*data)


    if data_check != data:
        data_check = data
        #toaster = ToastNotifier()
        #toaster.show_toast("Coronavirus {}".format(country) , message, duration = notification_duration , icon_path ="icon.ico")
        print("Coronavirus {}".format(country) , message,)
    
    else:
        time.sleep(refresh_time*60)
        #time.sleep(5)
        continue
