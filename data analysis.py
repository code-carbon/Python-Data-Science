import tkinter as tk
from tkinter import filedialog
from pandas import DataFrame

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Popularity':[1, 2, 0, 3],
        'Color':['Golden-mud','Fish Skin','Red Classic', 'White Havoc']
        }

df = DataFrame(cars, columns= ['Index','Brand', 'Price','Popularity','Color'])


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'wheat', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = True, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV ', command=exportCSV, bg='yellow', fg='black', font=('Papyrus', 12, 'bold'), height=5 , width=11)
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()