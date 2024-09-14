#Projeto para portifolio
#App com Custom TkInter + Api das Cotacoes + Matplotlib 
#Gabriel Campos Amaral Ribeiro 26/08/2024

#Biblioteca das janelas
import tkinter as tk
import customtkinter as ctk

#Bilioteca do tempo
import datetime as dt

#Importa a biblioteca dos graficos
import matplotlib.pyplot as plt

from moedas.bitcoin import bitcoin
from moedas.dollar import dollar
from moedas.euro import euro
from moedas.libra import libra
from moedas.peso_argentino import peso_argentino
from hora import hora

def janelaPrincipal():

  #Criando a janela 
  window=ctk.CTk()
  #Mudando a fonte da letra
  fonte = ctk.CTkFont(family="Monte", size=18, weight='bold') 
  #Muda o nome da janela
  window.title('COTAÇÕES BR')
  #Define o tamanho da janela
  window.geometry('300x400')
  #Não permite que aumentem o tamanho da janela
  window.resizable(False,False)
  #Texto do topo
  text=ctk.CTkLabel(window,text='COTAÇÕES PARA O REAL',font=fonte)
  #Coloca o texto na tela
  text.grid(padx=40,pady=10)

  #Texto da Introdução
  introducao=ctk.CTkLabel(window,text='MOEDAS:',font=fonte)
  #Coloca o texto na tela
  introducao.grid(padx=18,pady=10)

  #  ----- Botoes -----

  bt_dollar=ctk.CTkButton(window,text='Dollar',command=dollar)
  bt_dollar.grid(pady=5)

  bt_euro=ctk.CTkButton(window,text='Euro',command=euro)
  bt_euro.grid(pady=5)
  
  bt_bitcoin=ctk.CTkButton(window,text='Bitcoin',command=bitcoin)
  bt_bitcoin.grid(pady=5)

  bt_libra=ctk.CTkButton(window,text='Libra',command=libra)
  bt_libra.grid(pady=5)

  bt_peso = ctk.CTkButton(window, text='Peso Argentino',command=peso_argentino)
  bt_peso.grid(pady=5)

  #Texto Autor
  autor = ctk.CTkLabel(window, text='Desenvolvido por Gabriel Campos Amaral R.', font=ctk.CTkFont(family="Arial", size=10))
  autor.grid()
 
  #Mantem a janela em looping
  window.mainloop()
