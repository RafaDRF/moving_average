import tkinter as tk, tkinter.ttk as ttk
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as TkAgg
import numpy as np


top=tk.Toplevel()

view_nets = tk.Frame(top)
view_nets.pack(side='left',fill='both',expand=True) ## Packing Left in order to place
                                                    ## another Frame next to it

# Widgets
f = plt.Figure(figsize=(10,8),dpi=100)
F = f.add_subplot(111)

canvas = TkAgg.FigureCanvasTkAgg(f,master = view_nets) ## Moved Chart to view_nets Frame
canvas.show()
## canvas.get_tk_widget().grid(column = 0, row = 0) I'll explain commenting this out below

toolbar = TkAgg.NavigationToolbar2TkAgg( canvas, view_nets )
toolbar.update()
canvas._tkcanvas.pack(fill='both',expand=True)

## Adding Frame to bundle Treeview with Scrollbar (same idea as Plot+Navbar in same Frame)
tableframe = tk.Frame(top)
tableframe.pack(side='left',fill='y') ## Packing against view_nets Frame

COLUMNS=['name','value'] ## Column Headers for Data

## See Documentation for more info on Treeview
table=ttk.Treeview(tableframe, columns=COLUMNS, show='headings')
table.pack(side='left',fill='y')

for column in COLUMNS: ## Setting Column Header
    table.heading(column,text=column)

scroll=tk.Scrollbar(tableframe,command=table.yview) ## Adding Vertical Scrollbar
scroll.pack(side='left',fill='y')
table.configure(yscrollcommand=scroll.set) ## Attach Scrollbar