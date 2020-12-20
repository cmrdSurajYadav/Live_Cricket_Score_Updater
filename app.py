import requests
from bs4 import BeautifulSoup
from tkinter import *

url="https://www.mygov.in/covid-19/"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
page=requests.get(url,headers=headers)
sou=BeautifulSoup(page.content,'html.parser')
print(sou.prettify())
case=sou.find("div",class_="information_row").get_text()





print(case)
root=Tk()
root.geometry("444x555")

lo=Label(root,text=f"Active Case:-{case}",font=('arial',19,'bold'),fg="blue").pack()

# <button class="_2AkmmA _3-iCOr wvj5kH">NOTIFY ME</button>


root.mainloop()

