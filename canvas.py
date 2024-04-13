import tkinter as tk
from tkinter import ttk 

# Setup
window = tk.Tk()
window.geometry('100x100')
window.title('Canvas')




# canvas
canvas = tk.Canvas(window, bg= 'white')
canvas.pack()

def drawOnCanvas(event):
    x = event.x
    y = event.y
    brushSize = 1    
    canvas.create_oval((x - brushSize / 2, y - brushSize / 2, x + brushSize / 2, y + brushSize / 2), fill='black')

# Button
def clearCanvas():
    canvas.delete('all')

clearCanvasButton = ttk.Button(window, text='clear', command=clearCanvas)
clearCanvasButton.pack()


canvas.bind('<B1-Motion>', drawOnCanvas)
window.mainloop()