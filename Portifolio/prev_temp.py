# Gabriel Campos
# Utilizar a API da AwesomeAPI e o Streamlit

import streamlit as st
import requests as rq
import datetime as dt
import json as js

def run():
    def hora():
        # Pega a data e hora atuais
        hora = dt.datetime.now()
        data_hora = hora.strftime('%d/%m/%Y | %H:%M:%S')
        return data_hora

    def conversao(kelvin):
        # Converte a temperatura de Kelvin para Celsius
        celsius = kelvin - 273.15
        return celsius

    # Faz a requisição da previsão de temperaturas para os próximos 5 dias
    def previsao_temperatura(city, key='c745ca79c56d31ec5a4cad3751fb3514'):
        # Pega a latitude e longitude da cidade digitada
        link = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}'
        requisicao2 = rq.get(link)
        dados = requisicao2.json()
        
        lat = dados[0]['lat']
        lon = dados[0]['lon']

        # Através da longitude e latitude, a API consegue puxar a previsão do tempo somente dos próximos 5 dias
        link2 = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}'
        requisicao3 = rq.get(link2)
        dados2 = requisicao3.json()

        # Temperatura de hoje e assim por diante
        temperatura = dados2['list'][0]['main']['temp']
        # Conversão de Kelvin para Celsius
        temperatura = conversao(temperatura)

        # Temperatura dos próximos dias
        temperatura1 = conversao(dados2['list'][1]['main']['temp'])
        temperatura2 = conversao(dados2['list'][2]['main']['temp'])
        temperatura3 = conversao(dados2['list'][3]['main']['temp'])
        temperatura4 = conversao(dados2['list'][4]['main']['temp'])
        temperatura5 = conversao(dados2['list'][5]['main']['temp'])

        return temperatura, temperatura1, temperatura2, temperatura3, temperatura4, temperatura5, dados2

    def dia_semana():
        # Obtendo o dia da semana atual
        dia_primeiro = dt.datetime.now()
        dia_atual = dia_primeiro.strftime('%A')  

        # Obtendo o dia da semana + 1 
        primeiro = dia_primeiro + dt.timedelta(days=1)
        dia_da_semana1 = primeiro.strftime('%A')

        # Obtendo o dia da semana + 2
        segundo = dia_primeiro + dt.timedelta(days=2)
        dia_da_semana2 = segundo.strftime('%A')  

        # Obtendo o dia da semana + 3
        terceiro = dia_primeiro + dt.timedelta(days=3)
        dia_da_semana3 = terceiro.strftime('%A')  

        # Obtendo o dia da semana + 4
        quarto = dia_primeiro + dt.timedelta(days=4)
        dia_da_semana4 = quarto.strftime('%A')  

        # Obtendo o dia da semana + 5
        quinto = dia_primeiro + dt.timedelta(days=5)
        dia_da_semana5 = quinto.strftime('%A') 

        return dia_atual, dia_da_semana1, dia_da_semana2, dia_da_semana3, dia_da_semana4, dia_da_semana5

    def icon(dados, dados2):
        # Pega o ícone da condição climática
        icon_id = dados['weather'][0]['icon']         
        icon_url = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'

        icon_id1 = dados2['list'][1]['weather'][0]['icon']
        icon_url1 = f'https://openweathermap.org/img/wn/{icon_id1}@2x.png'

        icon_id2 = dados2['list'][2]['weather'][0]['icon']
        icon_url2 = f'https://openweathermap.org/img/wn/{icon_id2}@2x.png'

        icon_id3 = dados2['list'][3]['weather'][0]['icon']
        icon_url3 = f'https://openweathermap.org/img/wn/{icon_id3}@2x.png'

        icon_id4 = dados2['list'][4]['weather'][0]['icon']
        icon_url4 = f'https://openweathermap.org/img/wn/{icon_id4}@2x.png'
        
        # Ícone do dia 5
        icon_id5 = dados2['list'][5]['weather'][0]['icon']
        icon_url5 = f'https://openweathermap.org/img/wn/{icon_id5}@2x.png'
        
        return icon_url, icon_url1, icon_url2, icon_url3, icon_url4, icon_url5

    def descricao_condicao(dados, dados2):
        # Pega a descrição da condição climática
        descricao = dados['weather'][0]['description']
        descricao1 = dados2['list'][1]['weather'][0]['description']
        descricao2 = dados2['list'][2]['weather'][0]['description']
        descricao3 = dados2['list'][3]['weather'][0]['description']
        descricao4 = dados2['list'][4]['weather'][0]['description']
        descricao5 = dados2['list'][5]['weather'][0]['description']
        
        return descricao, descricao1, descricao2, descricao3, descricao4, descricao5

    # Aplicando CSS para mudar a fonte do texto
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
        
        .titulo {
            font-family: 'Open Sans', Courier, monospace;
            font-size: 50px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título da Página
    st.markdown("<h1 class='titulo' style='text-align: center;'>🌤️ Previsão do Tempo</h1>", unsafe_allow_html=True)

    # Caixa de texto
    city = st.text_input('Digite a cidade que deseja saber a condição climática:', max_chars=50).capitalize().strip()

    # Botão para pesquisar
    pesquisa = st.button('Consultar', use_container_width=True)

    if city:
        try:
            key = 'c745ca79c56d31ec5a4cad3751fb3514'
            link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
            requisicao = rq.get(link)
            dados = requisicao.json()
            
            # Verifica se a requisição retornou um erro
            if requisicao.status_code != 200:
                st.text('Cidade não encontrada ou erro na requisição.')
            else:
                # Pega a hora atual
                st.text(hora())
            
                #################################################
                # Puxa os dados das funções
                temperatura, temperatura1, temperatura2, temperatura3, temperatura4, temperatura5, dados2 = previsao_temperatura(city)
                dia_atual, dia_da_semana1, dia_da_semana2, dia_da_semana3, dia_da_semana4, dia_da_semana5 = dia_semana()
                icon_url, icon_url1, icon_url2, icon_url3, icon_url4, icon_url5 = icon(dados, dados2)
                descricao, descricao1, descricao2, descricao3, descricao4, descricao5 = descricao_condicao(dados, dados2)
                #################################################
        
                # Colunas e a proporção das colunas apresentadas na tela
                col1, col2 = st.columns([4, 5])  
                # Coluna 1
                with col1:
                    st.markdown(f'<h2 style="text-align: center; margin: 0;">{city.title()}</h2>', unsafe_allow_html=True)  # Cidade
                with col1: 
                    st.markdown(f'<h2 style="text-align: center; margin: 0;">{temperatura:.2f}°C</h2>', unsafe_allow_html=True)  # Temperatura
                with col1: 
                    st.markdown(f'<h4 style="text-align: center; margin: 0;">Condição: {descricao.capitalize()}</h4>', unsafe_allow_html=True)  # Condição
                # Coluna 2
                with col2:
                    st.markdown(f'<h4 style="text-align: center; margin: 0;">{dia_atual}</h4>', unsafe_allow_html=True)  # Texto do dia da semana
                with col2:
                    st.image(icon_url, width=280)  # Ícone

                col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  
                # Coluna 1
                with col1:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{dia_da_semana1}</h5>', unsafe_allow_html=True)  # Texto do dia da semana
                with col1:
                    st.image(icon_url1, width=100)  # Ícone
                with col1:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{temperatura1:.2f}°C</h5>', unsafe_allow_html=True)  # Temperatura
                with col1:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{descricao1.capitalize()}</h5>', unsafe_allow_html=True)  # Condição

                # Coluna 2
                with col2:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{dia_da_semana2}</h5>', unsafe_allow_html=True)
                with col2:
                    st.image(icon_url2, width=100)
                with col2:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{temperatura2:.2f}°C</h5>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{descricao2.capitalize()}</h5>', unsafe_allow_html=True)  # Condição

                # Coluna 3
                with col3:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{dia_da_semana3}</h5>', unsafe_allow_html=True)
                with col3:
                    st.image(icon_url3, width=100)
                with col3:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{temperatura3:.2f}°C</h5>', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{descricao3.capitalize()}</h5>', unsafe_allow_html=True)  # Condição

                # Coluna 4
                with col4:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{dia_da_semana4}</h5>', unsafe_allow_html=True)
                with col4:
                    st.image(icon_url4, width=100)
                with col4:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{temperatura4:.2f}°C</h5>', unsafe_allow_html=True)
                with col4:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{descricao4.capitalize()}</h5>', unsafe_allow_html=True)  # Condição

                # Coluna 5
                with col5:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{dia_da_semana5}</h5>', unsafe_allow_html=True)  # Texto do dia da semana
                with col5:
                    st.image(icon_url5, width=100)  # Ícone
                with col5:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{temperatura5:.2f}°C</h5>', unsafe_allow_html=True)  # Temperatura
                with col5:
                    st.markdown(f'<h5 style="text-align: center; margin: 0;">{descricao5.capitalize()}</h5>', unsafe_allow_html=True)  # Condição

        except KeyError:
            st.text('Erro ao processar os dados da cidade. Verifique se a cidade foi digitada corretamente.')
        except NameError: 
            st.text('Erro ao processar o nome da cidade. Verifique se a cidade foi digitada corretamente.')

    else:
        pass
