# Python program to create a table
  
from tkinter import *
from turtle import width
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=5, fg='black',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i+1, column=j+2)
                self.e.insert(END, lst[i][j])

# plot graph
fig = plt.Figure()

x = []
y = [4.1590,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1265,4.1807,4.1518,4.1643,4.1117,4.1293,4.0819,4.0346]

for i in range(len(y)):
    x.append(i)

# take the data
lst = [('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa'),
       ('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa'),
       ('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa'),
       ('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa'),
       ('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa'),
       ('04/06',4.88,'Alta'),
       ('04/06',8.44, 'Baixa')]



# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()

pedir_media = "Media Movel:"
pedido_media1 = Label(root, text=pedir_media, border= 10 )
entrada_media1 = Entry(root, width=5, justify='center')

pedido_media1.grid(column= 0, row=0)
entrada_media1.grid(column=1, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1, rowspan=10, columnspan=2)

ax = fig.add_subplot(111)
line, = ax.plot(x, y)

t = Table(root)
root.mainloop()