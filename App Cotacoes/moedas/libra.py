#Projeto para portifolio
#App com Custom TkInter + Api das Cotacoes + Matplotlib 
#Gabriel Campos Amaral Ribeiro 26/08/2024

#Biblioteca para fazer a requisição 
import requests as rq

#Biblioteca para tratar os dados vindos da API
import json as js

#Biblioteca das janelas
import tkinter as tk
import customtkinter as ctk

#Bilioteca do tempo
import datetime as dt

#Importa a biblioteca dos graficos
import matplotlib.pyplot as plt

#Importa a funcao que esta em outra pagina
from cotacao import cotacao,cotacao_libra
from hora import hora

def libra():
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
    
    
    #Texto 
    text=ctk.CTkLabel(window,text='LIBRA',font=fonte)
    #Coloca o texto na tela
    text.grid(padx=120,pady=15)

    #Texto 
    text=ctk.CTkLabel(window,text=f'COTAÇÃO: R$ {float(cotacao_libra()):.3f}',font=fonte)
    #Coloca o texto na tela
    text.grid()

    #Texto 
    text=ctk.CTkLabel(window,text=f'Data: {hora()}',font=ctk.CTkFont(size=12,weight='bold',family="Monte"))
    #Coloca o texto na tela
    text.grid()

    #Texto 
    text=ctk.CTkLabel(window,text='CONVERSÃO: ',font=fonte)
    #Coloca o texto na tela
    text.grid(padx=40,pady=5)

    #Conversao real para euro:
    conversao=ctk.CTkEntry(window,placeholder_text='DIGITE AQUI... (R$)')
    conversao.grid(pady=5)

    #Conversao euro para real:
    conversaoInversa=ctk.CTkEntry(window,placeholder_text='DIGITE AQUI... (£)')
    conversaoInversa.grid(pady=5)
    
    def converter():
        qnt_real=conversao.get()
        qnt_libra=conversaoInversa.get()
        resultado_texto=""

        try:
          if qnt_real :
            qnt_real=float(qnt_real)
            montante_libra=qnt_real/cotacao_libra()
            resultado_texto=f'R$ {qnt_real:.2f} -> {montante_libra:.2f} £'
          elif qnt_libra:
            qnt_libra=float(qnt_libra)
            montante_real=cotacao_libra()*qnt_libra
            resultado_texto=f'{qnt_libra:.2f} £ -> R$ {montante_real:.2f}'
          else:
            resultado_texto = 'Por favor, preencha um dos campos.'
        except ValueError:
            resultado_texto= 'Entrada inválida.'

        resultado.configure(text=resultado_texto)

    #Mostrar o resultado
    resultado = ctk.CTkLabel(window,text='')
    resultado.grid(pady=5)


    def mostrar_grafico():
      #Pega as 30 ultimas cotacoes da moeda
      ultimas_cotacoes=rq.get('https://economia.awesomeapi.com.br/json/daily/GBP-BRL/30')
      #Analisa os dados da requisicao
      conteudo_ultimas_cotacoes=ultimas_cotacoes.json()

      lista_ultimas_cotacoes=[]

      for valor in conteudo_ultimas_cotacoes:
        lista_ultimas_cotacoes.append(float(valor['bid']))

      # A lista fornecida está ao contrário, então inverte a lista
      lista_ultimas_cotacoes.reverse()

      # Cria uma lista de datas para o eixo x (30 dias atrás até hoje)
      hoje = dt.datetime.now()
      datas = []

      #Coloca as datas no grafico
      for i in range(len(lista_ultimas_cotacoes)):
        data = hoje - dt.timedelta(days=(29 - i))
        datas.append(data.strftime('%d/%m'))

      # Cria o gráfico
      #Define o tamanho do grafico
      plt.figure(figsize=(12, 6)) 
      # Linha com marcadores
      plt.plot(datas, lista_ultimas_cotacoes, 'b.--', marker='o')  
      #Coloca as gradezinhas no grafico
      plt.grid(True)
      #Titulo
      plt.title('Últimas 30 Cotações do libra (GBP/BRL)')
      #Nome eixo x
      plt.xlabel('Data')
      #Nome eixo y
      plt.ylabel('Cotação (R$)')
      # Rotaciona os rótulos do eixo x para melhor legibilidade
      plt.xticks(rotation=90) 
      plt.show()

    botao_converter = ctk.CTkButton(window, text='Converter', command=converter)
    botao_converter.grid(pady=5)

    #Botao para grafico
    botao=ctk.CTkButton(window,text='Gráfico últimas cotações',command=mostrar_grafico)
    botao.grid(pady=5)

    #Mantem a janela em looping
    window.mainloop()