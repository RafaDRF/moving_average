from tkinter import *

valores = [4.1590,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1265,4.1807,4.1518,4.1643,4.1117,4.1293,4.0819,4.0346]

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True


def enter(event):

    valor1 = entrada_media1.get()
    valor2 = entrada_media2.get()

    if isnumber(valor1) and isnumber(valor2):
        ambas_entrada_completas = valor1 != "" and valor2 != "" 

        if ambas_entrada_completas:
            entrada_media1.delete(0, 'end')
            entrada_media2.delete(0, 'end')
            media1 = media_movel_simples(valores,valor1)
            media2 = media_movel_simples(valores,valor2)
            print(media1)
            print(media2)


def media_movel_simples(valor, dias):
    dias = int(dias)
    ## dias maiores que valores
    if dias <= 0:
        return None
    
    total = 0

    for i in range(dias):
        total += valor[i]

    media = total/dias

    return media


janela = Tk()
janela.iconbitmap('icone.ico')
janela.title("Media Movel Simples")

pedir_media = "Media Movel:"
pedido_media1 = Label(janela, text=pedir_media, border= 10 )
entrada_media1 = Entry(janela, width=5, justify='center')

pedido_media1.grid(column= 0, row=0)
entrada_media1.grid(column=1, row=0)

entrada_media1.bind("<Return>", enter)

pedido_media2 = Label(janela, text=pedir_media, border= 10 )
entrada_media2 = Entry(janela, width=5, justify='center')

pedido_media2.grid(column= 0, row=1)
entrada_media2.grid(column=1, row=1)

entrada_media2.bind("<Return>", enter)

janela.mainloop()