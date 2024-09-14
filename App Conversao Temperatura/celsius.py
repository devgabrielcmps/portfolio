import customtkinter as ctk

def janela_conversao_para_celsius():
    
  def conversao_para_celsius():
    f = fahrenheit_celsius.get()

    try:
        c = (float(f) - 32) * (5 / 9)
        # Atualiza o label existente ao invés de recriá-lo
        resultado_conversao.configure(text=f'{f}°F -> {c:.2f}°C',font=fonte)
    except ValueError:
        resultado_conversao.configure(text="Por favor, insira um número válido.",font=fonte)

  def fechar_janela():
    window.destroy()

  #Cria a janela
  window=ctk.CTk()

  #Fonte
  fonte = ctk.CTkFont(family="Monte", size=18, weight='bold') 

  #Titulo da janela
  window.title('Fahrenheit for celsius')

  #Reestringe o tamanho da janela
  window.resizable(False,False)

  #Define o tamanho da janela
  window.geometry('500x400')

  #Texto cabecalho
  text=ctk.CTkLabel(window,text='Fahrenheit for celsius',font=ctk.CTkFont(family="Monte", size=25, weight='bold') )
  text.grid(padx=130,pady=40)

  #Botao de celsius para Fahrenheit
  #cursor=Troca o cursor pela maozinha,width e height aumenta o tamanho do botao
  fahrenheit_celsius=ctk.CTkEntry(window,placeholder_text='Temperatura em °F',width=200, height=50,font=fonte)
  fahrenheit_celsius.grid(pady=10)

  #Botao para confrimar
  botao_confirma=ctk.CTkButton(window,text='Converter',font=fonte,width=200,height=50,cursor="hand2",command=conversao_para_celsius)
  botao_confirma.grid(pady=10)

  resultado_conversao=ctk.CTkLabel(window,text='')
  resultado_conversao.grid(pady=5)

  botao_close_window=ctk.CTkButton(window,text='Fechar Janela',font=fonte,width=200,height=50,cursor="hand2",command=fechar_janela)
  botao_close_window.grid(pady=10)

  #Deixa a janela aberta
  window.mainloop()

