#Gabriel Campos 
#Criacao de um CRUD em python
# streamlit run Projetos2024\CRUD\index.py 

import streamlit as st

st.title('Cadastro User')

#Formulario
with st.form(key='include_cliente'):
  input_name=st.text_input(label='NOME')
  input_age=st.number_input(label='MEDIDAS:',format='%i',step=1)
  input_occupation=st.selectbox('PROFISSAO:',['1','2','3'])

  #Enviar para o banco de dados a informacao
  botao=st.form_submit_button('Entrar')

  
    



if botao == True:
  #Escreve na tela
  st.write(f'Nome: {input_name} | Idade: {input_age} | Number: {input_occupation}')
  # Criar um novo formulário com campos vazios
  with st.form(key='clear_fields'):
      st.form_submit_button('Limpar Campos')


#Menu lateral
st.sidebar.title('Menu')
pagSelect=st.sidebar.selectbox('Selecione a pagina',['Página 1','Pagina 2'])






