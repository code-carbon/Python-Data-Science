# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:31:23 2020

@author: Siva Prasad Murali
"""

import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame
n=int(input("~ "))
car=[]
city=[]
emission=[]
nameplate=[]
index=[]
for i in range(1,n+1):
    data=input("# ").split()
    car.append(data[0])
    city.append(data[1])
    emission.append(int(data[2]))
    nameplate.append(data[3])
    index.append(i)
        
cars = {'Index':index,
        'Brand': car,
            'City': city,
            'Emission':emission,
            'Nameplate':nameplate
            }


df = DataFrame(cars, columns=cars)


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'wheat', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV ', command=exportCSV, bg='yellow', fg='black', font=('Papyrus', 12, 'bold'), height=5 , width=11)
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()