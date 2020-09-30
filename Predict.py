import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr
from tkinter import *
from tkinter import messagebox

screen = Tk()

screen.configure(bg="midnight blue")
screen.title("EV FİYAT TAHMİNİ")
screen.geometry("550x350+500+300")
screen.resizable(False, False)
icon = PhotoImage(file="Image/predict.png")
screen.iconphoto(False, icon)

lblHomeSize=Label(text="KAÇ METRE KARE?",fg="white",bg="midnight blue",font=("Times 18 bold"))
lblHomeSize.place(x=15,y=25)

TxtlblPredict=Label(text="TAHMİN SONUCU: ",fg="white",bg="midnight blue",font=("Times 18 bold"))
TxtlblPredict.place(x=30,y=280)

entryHomeSize=Entry(font=("Times 18 bold"))
entryHomeSize.place(x=280,y=25)

lblPredict=Label(fg="white",bg="midnight blue",font=("Times 25 bold"))
lblPredict.place(x=260,y=275)

def prediction():
    # formula: mx+b
    dataset = pd.read_csv("Dataset/housePrice.csv")

    x = dataset["metrekare"]
    y = dataset["fiyat"]
    x = x.values.reshape(99, 1)
    y = y.values.reshape(99, 1)

    lineerRegression = lr()
    lineerRegression.fit(x, y) # Eğitim
    lineerRegression.predict(x) # Metrekare değerine göre tahmin işlemi.

    # Denklem değerlerinin elde edilmesi:
    m = lineerRegression.coef_
    b = lineerRegression.intercept_

    try:
        metreKare =int(entryHomeSize.get())
        tahmin = m * metreKare + b
        lblPredict["text"] = int(tahmin),"000","TL"
    except ValueError:
        messagebox.showinfo("UYARI!!!","Lütfen Sayısal Bir Değer Girin !!!")

    # plt.scatter(x,y)
    # plt.scatter(metreKare,tahmin,c="lime",marker="*")
    # plt.show()

btnPredict = Button(text="TAHMİN YAP",font=("Times","15","bold") ,bg="yellow",fg="black",width=25,height=4,command=prediction)
btnPredict.place(x=120,y=120)

mainloop()