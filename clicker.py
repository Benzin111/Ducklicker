#(RU)
#ДЛЯ ЭПИЛЕПТИКОВ - ДИСКЛЕЙМЕР! ПРИ АКТИВАЦИИ МАРИХУАНЫ БУДЕТ РЕЗКОЕ МЕРЦАНИЕ ЦВЕТОВ! БУДЬТЕ ОСТОРОЖНЫ! В СЛУЧАЕ ПОЛУЧЕНИЕ УЩЕРБА - ЗАКРЫВАЙТЕ ИГРУ (И ОБРАТИТЕСЬ К ВРАЧУ)!!!
#В ДАННОМ СЛУЧАЕ Я НЕ НЕСУ ОТВЕТСТВЕННОСТЬ! УЧТИТЕ, ГОСПОДА!

#(ENG)
#FOR EPILEPTICS - DISCLAIMER! WHEN MARIJUANA IS ACTIVATED, THERE WILL BE A SHARP FLICKER OF COLORS! BE CAREFUL! IN CASE OF DAMAGE, CLOSE THE GAME (AND CONSULT A DOCTOR)!!!
#IN THIS CASE, I AM NOT RESPONSIBLE! CONSIDER!


#ITS MY FIRST CLICKER. CONSIDER, ITS BETA TEST!

import tkinter as tk
import random as rnd
from threading import Thread
import time as tm

#Функция счета кликов
def click():
    global clicks
    global add_click
    clicks += add_click
    quantity_clicks["text"] = f"Quality clicks: {clicks}"


#Функция покупки Марихуаны и действие марихуаны
def MARIJUANA():
    global root
    global clicks
    if clicks >= 200:
        clicks -= 200
        quantity_clicks["text"] = f"Quality clicks: {clicks}"
        Thread(target=randon_bg_colors).start()

def randon_bg_colors():
    colors = ["Red", "Blue", "Green", "Yellow", "Black"]
    global rbCol
    rbCol = False
    for i in range(400000):
        root["bg"] = rnd.choice(colors)
        tm.sleep(0.0000001)
        if rbCol:
            break
    root["bg"] = "Black"

#Действия, которые нужно выполнить перед закрытием окна
def on_closing():
    global rbCol
    rbCol = True
    root.destroy()

#Функция которая покупает кликов и добавляет его
def adding_click():
    global add_click
    global clicks
    global buyclick
    if clicks >= buyclick:
        add_click += 1
        clicks -= buyclick
        quantity_clicks["text"] = f"Quality clicks: {clicks}"
        buyclick += 15
        button2["text"] = f"Buy click ({buyclick} clks)"

#Окно
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.config(bg= "black")
root.title("Ducklicker")
root.geometry("340x500")
root.resizable(False, False)
logo = tk.PhotoImage(file= "logophoto/logoduckclicker.png")
root.iconphoto(False, logo)
#Главный текст
text1 = tk.Label(root, text= "Ducklckome to clicker! Click him! ↓↓↓",
                 bg= "black",
                 fg= "White",
                 font=("Lucida Console", 9, "bold"))

#Количество кликов
clicks = 0
quantity_clicks = tk.Label(root, text= f"Quality clicks: {clicks}",
                           bg = "Black",
                           fg= "#F9EF99",
                           font=("Lucida Console", 9, "bold",),
                           pady= 10)
#Кнопка клика
duck = tk.PhotoImage(file= "models/duck1.png")
button = tk.Button(root,
                   bg= "black",
                   image= duck,
                   activebackground= "#E6DC7B",
                   padx= 20,
                   pady= 20,
                   anchor= "se",
                   command= click)
#Покупка МАРИХУАНЫ
marijuana = 200
button1 = tk.Button(root,
                    bg= "blue",
                    fg= "Red",
                    activebackground= "Green",
                    activeforeground= "Yellow",
                    text= "MARIJUANA (200 clks)",
                    command= MARIJUANA
                    )
#Покупки кликов
buyclick = 10
add_click = 1
button2 = tk.Button(root,
                    bg = "black",
                    fg = "white",
                    activebackground= "gray",
                    activeforeground= "white",
                    text= f"Buy click ({buyclick} clks)",
                    command= adding_click)

#Упаковки и прочее
text1.pack()
quantity_clicks.pack()
button.pack()
button1.pack()
button2.pack()
root.mainloop()