# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np
import urllib    ## Save image from image url


page = requests.get('http://covid-19.moh.gov.my/terkini').text
soup = BeautifulSoup(page,'html.parser')      #Get page source

title = soup.findAll("h2",{"class":"p-name"})[0]
title=title.findAll("a",{"class":"u-url"})
t=title[0]
title=t.text

imge= soup.findAll("div",{"class":"list-blog-padding"})[0]
imge=imge.findAll("div")[2]
img=str(imge)

lk = img.split('<img alt="" src="',1)[1]     #New Cases
lk1= lk.split('></div>',1)[0]
moh= "http://covid-19.moh.gov.my/" 
lkFinal = moh + lk1

response = requests.get(lkFinal)  ## Save image from image url
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

# lkFinal="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/30mac.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/31mac.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/1april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/2april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/3april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/4april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/5april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/6april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/7april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/8april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/9april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/10april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/11april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/12april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/13april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/14april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"
# lkFinal ="https://github.com/hafiz1230/eMakerthon-Firestore/blob/main/infographic/15april.jpg?raw=true"
# title="Situasi Terkini COVID-19 di Malaysia 15 April 2021"


data={

     "image" : "",
     "title" : title
     
}

# ###------------------------------------------------Upload to firebase-------------------------------###
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Singapore')
time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

cred = credentials.Certificate(".json")
firebase_admin.initialize_app(cred)
db=firestore.client()

db.collection("Infographic").document("982").set(data)   ## Store in firestore

