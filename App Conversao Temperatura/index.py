#Conversor de temperatura entre celsius para Fahrenheit e vice-versa
#Projeto para portifolio

import customtkinter as ctk
from celsius import janela_conversao_para_celsius
from fahrenheit import janela_conversao_para_fahrenheit


def janelaPrincipal():

  #Cria a janela
  window=ctk.CTk()

  #Fonte
  fonte = ctk.CTkFont(family="Monte", size=18, weight='bold') 

  #Titulo da janela
  window.title('Conversor de Temperatura')

  #Reestringe o tamanho da janela
  window.resizable(False,False)

  #Define o tamanho da janela
  window.geometry('500x400')

  #Texto cabecalho
  text=ctk.CTkLabel(window,text='CONVERSOR DE TEMPERATURA',font=fonte)
  text.grid(padx=110,pady=40)

  #Botao de celsius para Fahrenheit
  #cursor=Troca o cursor pela maozinha,width e height aumenta o tamanho do botao
  botao_celsius_fahrenheit=ctk.CTkButton(window,text='°C -> °F',font=fonte,width=200, height=50,cursor="hand2",command=janela_conversao_para_fahrenheit)
  botao_celsius_fahrenheit.grid(pady=10)

  #Botao de Fahrenheit para celsius
  botao_fahrenheit_celsius=ctk.CTkButton(window,text='°F -> °C',font=fonte,width=200, height=50,cursor="hand2",command=janela_conversao_para_celsius)
  botao_fahrenheit_celsius.grid(pady=10)


  #Deixa a janela aberta
  window.mainloop()


janelaPrincipal()



