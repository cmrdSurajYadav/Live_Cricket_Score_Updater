import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

from requests.api import head

# content=""


def update():
    try:
        url='https://www.cricbuzz.com/'

        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

        page=requests.get(url,headers=headers)

        content=BeautifulSoup(page.content,'html.parser')
        team1_score=content.find("div",class_="cb-hmscg-bat-txt").get_text()
        team2=content.find("div",class_="cb-hmscg-bwl-txt").get_text()
        try:

            livetext=content.find("div",class_="cb-text-live").get_text()

            foot.config(text=livetext)
        except:

            livetext=content.find("div",class_="cb-text-complete").get_text()

            foot.config(text=livetext)





        l.config(text=team1_score)
        l2.config(text=team2)
    except:
        messagebox.showerror("connection","Please Check Your Internet Connection Or Try Again Letter")
        
    


root=Tk()


# <div class=" cb-ovr-flo cb-text-live">Gemcon Khulna opt to bat</div>
# title=content.find("div",class_="cb-text-live").get_text()
root.title("Live Cricket Score By Suraj")

root.resizable(0,0)
file=PhotoImage(file="—Pngtree—illustration of batsman and bowler_4183426.png")
background=Label(root,image=file)
background.pack()
try:
    
    url='https://www.cricbuzz.com/'

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    page=requests.get(url,headers=headers)

    content=BeautifulSoup(page.content,'html.parser')



    team1_score=content.find("div",class_="cb-hmscg-bat-txt").get_text()

# team2=content.find("div",class_="cb-hmscg-bat-txt cb-hmscg-tm-nm").get_text()
# <div class="cb-hmscg-bwl-txt "><div class="cb-ovr-flo cb-hmscg-tm-nm">RJSH..</div><div class="cb-ovr-flo" style="display:inline-block; width:140px"></div></div>
    team2=content.find("div",class_="cb-hmscg-bwl-txt").get_text()



    head=Label(text="Cricko",font=('bold',20),bg="black",fg="blue")
    head.place(x=165,y=60)
    try:
         livetext=content.find("div",class_="cb-text-live").get_text()
         foot=Label(text=livetext,font=('bold',15),bg="black",fg="blue")
         foot.pack(fill=X)
    except:
         livetext=content.find("div",class_="cb-text-complete").get_text()
         foot=Label(text=livetext,font=('bold',15),bg="black",fg="blue")
         foot.pack(fill=X)
   
    l=Label(text=team1_score,font=('bold',15),bg="black",fg="red")
    l.place(x=50,y=330)

    l2=Label(text=team2,font=('bold',15),bg="black",fg="red")
    l2.place(x=50,y=360)

    refresh=Button(text="Refresh",font=('bold',15),bg="black",fg="green",command=update)
    refresh.place(x=290,y=345)
except:
    messagebox.showerror("connection","Please Check Your Internet Connection Or Try Again Letter")
    



root.mainloop()


