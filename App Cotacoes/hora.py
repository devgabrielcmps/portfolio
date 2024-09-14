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


def hora():
  #Pega a data e hora atuais
  hora=dt.datetime.now()
  data_hora=hora.strftime('%d/%m/%Y | %H:%M:%S')
  return data_hora
