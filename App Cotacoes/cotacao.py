#Projeto para portifolio
#App com Custom TkInter + Api das Cotacoes + Matplotlib 
#Gabriel Campos Amaral Ribeiro 26/08/2024

#Biblioteca para fazer a requisição 
import requests as rq

#Biblioteca para tratar os dados vindos da API
import json as js

def cotacao():
  link='https://economia.awesomeapi.com.br/json/all'
  cotacoes=rq.get(link)
  conteudo=cotacoes.json()

  return conteudo


#Pega os valores mais atuais das moedas

def cotacao_euro():
  #Pega o valor mais atual da moeda
  cotacao_euro=cotacao()['EUR']['bid']
  cotacao_euro=float(cotacao_euro)

  return cotacao_euro

def cotacao_dollar():
  cotacao_dollar=cotacao()['USD']['bid']
  cotacao_dollar=float(cotacao_dollar)

  return cotacao_dollar

def cotacao_bitcoin():
  cotacao_bitcoin=cotacao()['BTC']['bid']
  cotacao_bitcoin=float(cotacao_bitcoin)

  return cotacao_bitcoin

def cotacao_libra():
  cotacao_libra=cotacao()['GBP']['bid']
  cotacao_libra=float(cotacao_libra)

  return cotacao_libra

def cotacao_peso_argentino():
  cotacao_peso_argentino=cotacao()['ARS']['bid']
  cotacao_peso_argentino=float(cotacao_peso_argentino)

  return cotacao_peso_argentino

