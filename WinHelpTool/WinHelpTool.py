import tkinter as tk
import playsound
from PIL.ImageTk import PhotoImage
import pyautogui as pg
import time
import os


os.system("title WinHelpTool SHELL")

def cmd():
    os.system("cmd")
    print("started COMMAND PROMPT")

def chrome():
    os.startfile("chrome.exe")
    print("started CHROME")

def xampp():
    os.chdir("C:/xampp")
    os.startfile("xampp-control.exe")
    print("started XAMPP CONTROL PANEL")

def python():
    os.startfile("python.exe")
    print("started PYTHON")

def settings():
    os.system("start ms-settings:")
    print("started ms-settings:")

def calc():
    os.system("calc")
    print("started CALCULATOR")

def brave():
    os.startfile("brave.exe")
    print("started BRAVE BROWSER")


window = tk.Tk()
window.title("WinHelpTool")
window.iconbitmap("windows.ico")
window.geometry("600x400")
window.tk_setPalette("#FFFFFF")
img2 = tk.PhotoImage(file="CHROME.png")
img3 = tk.PhotoImage(file="xamppphoto.png")
img4 = tk.PhotoImage(file="python.png")
img5 = tk.PhotoImage(file="windows.png")
img6 = tk.PhotoImage(file="calc.png")
img7 = tk.PhotoImage(file="Brave_lion.png")
button2 = tk.Button(text = "CHROME", image = img2, compound="top", command = chrome)
button2.pack(side = "left")
button3 = tk.Button(text = "XAMPP", image = img3, compound = "top", command = xampp)
button3.pack(side = "left")
button4 = tk.Button(text = "PYTHON", image = img4, compound = "top", command = python)
button4.pack(side = "left")
button5 = tk.Button(text = "SETTINGS", image = img5, compound = "top", command = settings)
button5.pack(side = "left")
button6 = tk.Button(text = "CALCULATOR", image = img6, compound = "top", command = calc)
button6.pack(side = "left")
button7 = tk.Button(text = "BRAVE", image = img7, compound= "top", command = brave)
button7.pack(side = "left")

window.mainloop()