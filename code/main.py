import tkinter as tk

import gui
import sets

def update(button):
    global frameGraph, frameSetting, set
    
    if button == "render":
        set = eval("sets."+frameSetting.setting("set"))
    frameGraph.size(int(frameSetting.setting("width")), int(frameSetting.setting("accuracy")))
    frameGraph.draw(set)

set = []   

window = tk.Tk()
window['bg'] = 'white'

frameGraph = gui.Graph(window, bg="#fafafa", borderwidth=2, relief="groove")
frameGraph.grid(row=0, column=1, padx=10)

frameSetting = gui.Settings(window, bg="#fafafa", borderwidth=2, relief="groove")
frameSetting.grid(row=0, column=0, padx=10)
frameSetting.callback = update
frameSetting.update("render")

window.mainloop()
