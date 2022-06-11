#---------Imports
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import matplotlib.pyplot as plt
#---------End of imports

fig = plt.Figure()

x = []
y = [4.1590,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1265,4.1807,4.1518,4.1643,4.1117,4.1293,4.0819,4.0346]

for i in range(len(y)):
    x.append(i)

root = Tk.Tk()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)


pedir_media = "Media Movel:"
pedido_media1 = Tk.Label(root, text=pedir_media, border= 10 )
entrada_media1 = Tk.Entry(root, width=5, justify='center')

pedido_media1.grid(column= 0, row=0)
entrada_media1.grid(column=1, row=0)


ax = fig.add_subplot(111)
line, = ax.plot(x, y)

y = [2,7,5,5,7,9,4,5,4,4.1265,7,8,6,4.1117,4.1293,8,4.0346]
line2, = ax.plot(x, y,color="red")

Tk.mainloop()