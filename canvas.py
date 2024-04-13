import tkinter as tk
from tkinter import ttk 

# Setup
window = tk.Tk()
window.geometry('500x500')
window.title('Canvas')




# canvas
canvas = tk.Canvas(window, width=400, height=400, bg= 'black')
canvas.pack(pady=50, padx=50)

def drawOnCanvas(event):
    x = event.x
    y = event.y
    brushSize = 10  
    canvas.create_oval((x - brushSize / 2, y - brushSize / 2, x + brushSize / 2, y + brushSize / 2), fill='white', outline='white')

# Button
def clearCanvas():
    canvas.delete('all')

clearCanvasButton = ttk.Button(window, text='clear', command=clearCanvas)
clearCanvasButton.pack()


canvas.bind('<B1-Motion>', drawOnCanvas)
window.mainloop()