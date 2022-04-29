import tkinter
from tkinter import*
import random
import time 

renkler =[["yellow","sarı"],["green","yeşil"],["red","kırmızı"],["blue","mavi"],["black","siyah"],["purple","mor"]]

skor = 0 
kalan_sure = 60


def basla(event):
    if kalan_sure == 60:
        say() #sürenin azalmasını sağlar
    
    yeni_renk()

def yeni_renk():
    global skor
    global kalan_sure

    if kalan_sure > 0 :

        if giris.get().lower() == renkler[1][1].lower() :
            skor += 1  
        giris.delete(0,tkinter.END)
        random.shuffle(renkler) # Listedeki strinleri rastegele değşştirir

        etiket.config(fg = str(renkler[1][0]),text = str(renkler[0][1]))
        skor_etiketi.config(text = "Skor: " + str(skor))

def say():
    global kalan_sure

    if kalan_sure >0 :
        kalan_sure -= 1 
        sure_etiketi.config(text = "Kalan Süre : "+ str(kalan_sure))
        sure_etiketi.after(1000,say)

    elif kalan_sure < 0 :
            time.sleep(3)
            pencere.destroy()
   



pencere = Tk()
pencere.title("Renk Tahmin Oyunu")
pencere.geometry("450x350")

aciklama = tkinter.Label(pencere,text = "Kelimelerin rengini gir, Kelimeyi yazma",font=("Helvatica",12))
aciklama.pack()

skor_etiketi = tkinter.Label(pencere,text ="Başlamak için entere basınız",font = ("Helvetica",12))
skor_etiketi.pack()

sure_etiketi = tkinter.Label(pencere,text = "Kalan sure :" + str(kalan_sure),font = ("Helvetica",12))
sure_etiketi.pack()

dugme = Button(pencere,text = "Çıkış",command =pencere.destroy)
dugme.pack()

etiket = tkinter.Label(pencere , font = ("Helvetica",55))
etiket.pack()

giris  = tkinter.Entry(pencere)

pencere.bind("<Return>",basla)
giris.pack()

giris.focus_set()
pencere.mainloop()


















