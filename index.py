from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator
from urllib import response
from PIL import ImageTk, Image

#importando bibliotecas api
import requests
import time
import json



co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue

fundo="#484f60"

#criando janela
janela=Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)
#dividindo janela
ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)


frame_cima=Frame(janela,width=320,height=50,bg=co1,pady=0,padx=0, relief='flat')
frame_cima.grid(row=1,column=0)

frame_baixo=Frame(janela,width=320,height=300,bg=fundo,pady=0,padx=0, relief='flat')
frame_baixo.grid(row=2,column=0,sticky=NW)
#funcao 
def info():
        api_link='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL'
        response=requests.get(api_link)

        #convertando os dados em dicionario

        dados= response.json()

        #valor USD

        valor_usd=float(dados['USD'])
        valor_formatado_usd="${:,.3f}".format(valor_usd)
        label_p_usd['text']=valor_formatado_usd
        
        frame_baixo.after(1000,info)
        
        #valor eua

        valor_eua=float(dados['EUR'])
        valor_formatado_eua="€ {:,.3f}".format(valor_eua)
        label_p_eua['text']=valor_formatado_eua
        #valor br

        valor_real=float(dados['BRL'])
        valor_formatado_real="R$ {:,.3f}".format(valor_real)
        label_p_reais['text']=valor_formatado_real

        #valor kz

        valor_aoa=float(dados['AOA'])
        valor_formatado_aoa="Kz {:,.3f}".format(valor_aoa)
        label_p_kz['text']=valor_formatado_aoa


#configurando frame cima
imagem=Image.open('bitcoin.png')
imagem=imagem.resize((30,30),Image.ANTIALIAS)
imagem=ImageTk.PhotoImage(imagem)

label_icon=Label(frame_cima,image=imagem,compound=LEFT,bg=co1,relief='flat')
label_icon.place(x=10,y=10)

label_nome=Label(frame_cima,text='Bitcoin Price Tracker',bg=co1,relief='flat',anchor='center',font=('Arial 20'),fg=co2)
label_nome.place(x=50,y=5)

#configurando frame baixo

label_p_usd=Label(frame_baixo,text='',bg=fundo,width=14,relief='flat',anchor='center',font=('Arial 20'),fg=co1)
label_p_usd.place(x=0,y=50)

label_p_eua=Label(frame_baixo,text='',bg=fundo,width=14,relief='flat',anchor='center',font=('Arial  12'),fg=co1)
label_p_eua.place(x=10,y=130)

label_p_reais=Label(frame_baixo,text='',bg=fundo,width=14,relief='flat',anchor='center',font=('Arial 12'),fg=co1)
label_p_reais.place(x=10,y=160)

label_p_kz=Label(frame_baixo,text='',bg=fundo,width=14,relief='flat',anchor='center',font=('Arial 12'),fg=co1)
label_p_kz.place(x=10,y=190)

info()

janela.mainloop()

