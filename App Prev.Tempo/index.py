import requests as rq
import streamlit as st

#Titulo da Pagina
st.title('Previsao do tempo')


url = f'https://api.openweathermap.org/data/2.5/onecall?lat={coordenadas.latitude}&lon={coordenadas.longitude}&exclude=current,minutely,hourly,alerts&units=metric&appid={key}'
response = rq.get(url)
dados2 = response.json()


def coordenadas(city, api_key='88f9ee706197160c65aff2e93f7c0e19'):
    # URL do endpoint de previsão atual
    link=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=pt_br'
    # Fazendo a requisição para a API
    response = rq.get(url)
    dados = response.json()
    
    # Extraindo latitude e longitude
    latitude = dados['coord']['lat']
    longitude = dados['coord']['lon']
    
    return latitude, longitude

